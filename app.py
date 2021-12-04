import re
from  flask import Blueprint
from flask import Flask, config,render_template,redirect,url_for,request
import os
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

@app.route('/')
def kid():
    return render_template('index.html')
@app.route('/alphabet')
def alphabet():
    return render_template('alphabet.html')  
@app.route('/numbers')
def numbres():
    return render_template('numbers.html')   
@app.route('/pronounce')
def pronounce():
    return render_template('pronounce.html')  
@app.route('/games')
def games():
    return render_template('games.html', methods=['GET','POST'])   
@app.route('/about')
def about():
    return render_template('about.html')       



if __name__=="__main__":
    app.run(debug=True)    