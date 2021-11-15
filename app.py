#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 01:45:26 2021

@author: nir
"""

from flask import Flask, render_template, request, Response
from  ChuckNorrisJokes import Random_Joke, Catgory_Joke, All_Categories, Catgory_Joke1 ,FreeSearch1
import boto3 

app = Flask(__name__)


dynamodb = boto3.resource('dynamodb')

from boto3.dynamodb.conditions import Key, Attr

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['post'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        table = dynamodb.Table('users')
        
        table.put_item(
                Item={
        'name': name,
        'email': email,
        'password': password
            }
        )
        msg = "Registration Complete. Please Login to your account !"
    
        return render_template('login.html',msg = msg)
    return render_template('index.html')

@app.route('/login')
def login():    
    return render_template('login.html')


@app.route('/check',methods = ['post'])
def check():
    x=''
    alljokecat = All_Categories()
    search = FreeSearch1(x)
    
    if request.method=='POST':
        
        email = request.form['email']
        password = request.form['password']
        
        table = dynamodb.Table('users')
        response = table.query(
                KeyConditionExpression=Key('email').eq(email)
        )
        items = response['Items']
        name = items[0]['name']
        print(items[0]['password'])
        if password == items[0]['password']:
            
            return render_template("home.html", alljokecat = alljokecat, search = search, name = name)
    return render_template("login.html")


@app.route('/home', methods=['GET', 'POST'])

def home():
    x = ''
    result = Catgory_Joke1(x)
    alljokecat = All_Categories()
    if request.method == "POST":
        select = request.form.get("x")
        result = Catgory_Joke1(select)
        
                      
    return render_template('home.html', alljokecat = alljokecat, result = result)

@app.route('/search', methods=['GET', 'POST'])
def search():
    search1= ''
    x = ''
    
    #jokes1 = []
    alljokecat = All_Categories()
    search = FreeSearch1(x)
    if request.method == "POST":
        freesearch = str(request.form["x"])
        search1 = FreeSearch1(freesearch)
        
    
    return render_template('home.html', alljokecat= alljokecat , search1 = search1)


@app.route('/random', methods=['POST'])
def random():
    alljokecat = All_Categories()
    joke = Random_Joke()
    processed_text = joke
    return render_template('home.html', alljokecat= alljokecat , processed_text = processed_text)

@app.route('/upload', methods=['POST'])
def my_form_post():
    joke = Random_Joke()
    processed_text = joke
    # Some internal stuff with processed text
    return render_template('index.html', processed_text=processed_text)


#@app.route('/joke1', methods =['POST'])




if __name__ == "__main__":
    
    app.run(debug=True)




