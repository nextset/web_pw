from flask import Flask, render_template
from main import pw

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    a = [pw() for x in range(95)]
    return render_template('index.html', a=a)