from flask import render_template
from app import app

@app.route('/')
def index():
    message = 'Hello World!'
    return render_template('index.html', message1 = message)
    title = 'Home - News Highlights'
    return render_template('index.html', title = title)

@app.route('/news/<news_id>')
def news(news_id):
    return render_template('news.html', id = news_id )
    heading = 'News - More News!'
    return render_template('news.html', heading = heading )
