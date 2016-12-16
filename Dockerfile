FROM python:3
ADD ./src/main.py ./src/
CMD [ "python", "./src/main.py"]
