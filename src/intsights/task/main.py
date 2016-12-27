import daemon
class MyDaemon(object):
    def __init__(self, runner, sleep_minutes):
        self.runner = runner
        self.sleep_minutes = sleep_minutes
        
    def run(self):
        with daemon.DaemonContext():
            self.runner.run(self.sleep_minutes)

if __name__ == '__main__':
    from .runner import Runner
    sleep_minutes = 4*60
    MyDaemon(Runner(),sleep_minutes).run()


