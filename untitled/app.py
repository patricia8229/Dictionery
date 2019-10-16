from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLALchemy #import sqlalchemy

#importing the configuration
from configs.config import development, production

app = Flask (__name__)

#setting the config class to be used
app.config.from_object(Development)
#sql-alchemy instance
db = SQLALchemy (app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
