from app import app
from flask import render_template



@app.route('/')
def index():
    return render_template('index.html')




@app.route('/page2')
def page2():
    favs = ['Naruto', 'Full Metal Alchemist', 'Death Note', 'One Piece', 'Black Clover']


    return render_template('page2.html', favs = favs)