import uuid
import pytz, datetime, dateutil

class DB:
    def __init__(self):
        self.normalizer = self.Normalizer()
        self.table = None

    def lazy_init_table(self):
        if self.table is None:
            self.table = self._init_table()

    def insert_paste(self, author, title, content, date_str, date_tz_str):
        author = self.normalizer.normalize_author(author)
        title = self.normalizer.normalize_text(title)
        content = self.normalizer.normalize_text(content)
        date = self.normalizer.normalize_date(date_str, date_tz_str)
        exist_paste_content = self._select_content(title)
        if exist_paste_content is not None:
            if exist_paste_content == content:
                return
            else:
                title += str(uuid.uuid4()).replace('-', '')[0:7]
        self._insert_paste(author, title, content, date)

    def _select_content(self, title):
        self.lazy_init_table()
        i = self.table.select()

    @staticmethod
    def _init_table():
        import sqlalchemy
        import sqlalchemy.types as sqltypes

        db = sqlalchemy.create_engine('sqlite:///pastes.db')
        db.echo = False
        metadata = sqlalchemy.MetaData(db)
        table = sqlalchemy.Table('pastes', metadata,
                                 sqlalchemy.Column('title', sqltypes.String(32), primary_key=True),
                                 sqlalchemy.Column('author', sqltypes.String(32)),
                                 sqlalchemy.Column('content', sqltypes.String(32)),
                                 sqlalchemy.Column('date_str', sqltypes.String(32)),
                                 )
        table.create(checkfirst=True)
        return table

    def _insert_paste(self, author, title, content, date_str):
        self.lazy_init_table()
        i = self.table.insert()
        i.execute(author, title, content, date_str)

    class Normalizer:
        empty_author = set(['guest', 'unknown', 'anonymous'])
        empty_author_name = ''
        strftime_fmt = '%Y-%m-%d %H:%M:%S'

        def __init__(self):
            pass

        def normalize_author(self, author_name):
            author_name = self.normalize_text(author_name)
            if author_name.lower() in self.empty_author:
                author_name = self.empty_author_name
            return author_name

        def normalize_text(self, text):
            text = text.lstrip().rstrip()
            return text

        def normalize_date(self, date_str, date_tz_str):
            parsed = dateutil.parser.parser.parse(date_str)
            naive_date = parsed.date()
            local = pytz.timezone(date_tz_str)
            local_dt = local.localize(naive_date)
            utc_dt = local_dt.astimezone(pytz.utc)
            return utc_dt.strftime(self.strftime_fmt)




