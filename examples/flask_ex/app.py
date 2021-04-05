from flask import Flask
from huey import RedisHuey
from huey import SqliteHuey


DEBUG = True
SECRET_KEY = 'shhh, secret'

app = Flask(__name__)
app.config.from_object(__name__)

# huey = RedisHuey()
huey = SqliteHuey(filename='/Users/xubiao/Downloads/huey-master/examples/flask_ex/demo.db')
