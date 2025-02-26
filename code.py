from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Миссия Колонизация Марса',
                           phrase='И на Марсе будут яблони цвести!')


@app.route('/training/<prof>')
def odd_even(prof):
    return render_template('profs.html', prof=prof)


@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    return render_template('for.html', news=news_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
