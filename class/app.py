from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

@app.route('/user/<string:patricia>')
def user(username):
    return 'The user is called ()',format (username)

