#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:16:13 2021

@author: nir
"""
import json
import requests
import pandas as pd
####ChuckNorris JOKES app
def Random_Joke():
    random = requests.get("https://api.chucknorris.io/jokes/random")
    Random = random.text
    random_dict = json.loads(random.text)
    randomdf = pd.DataFrame(random).to_dict()
    
    for i in random_dict:
        if i == "value":
            print(random_dict[i])
    return random_dict[i]

def Catgory_Joke():
    x = input("Enter Category:")
    categories =  requests.get("https://api.chucknorris.io/jokes/random?category=" + x)
    Categories = categories.text
    categories_dict = json.loads(categories.text)
    categorydf = pd.DataFrame(categories).to_dict()
    
    for i in categories_dict:
        if i == "value":
            print(categories_dict[i])
    return categories_dict[i]

def Catgory_Joke1(x):
    
    categories =  requests.get("https://api.chucknorris.io/jokes/random?category=" + x)
    Categories = categories.text
    categories_dict = json.loads(categories.text)
    categorydf = pd.DataFrame(categories).to_dict()
    
    for i in categories_dict:
        if i == "value":
            print("")
    return categories_dict[i]

def All_Categories():
    AllCategories = requests.get("https://api.chucknorris.io/jokes/categories")
    categories_dict = json.loads(AllCategories.text)
    list1 = []
    for i in categories_dict: 
        list1.append(i)
        #print(i)
    return list1

def FreeSearch():
    x = input("Free Search:")
    freesearch = requests.get("https://api.chucknorris.io/jokes/search?query=" + x)
    freesearch_dict =  json.loads(freesearch.text)
    for key, value in freesearch_dict.items():    
        if key == "result":
            for subvalue in value:                
                for i in subvalue:
                    if i == "value":                        
                        print(subvalue[i])
                        print('*****')
    return subvalue[i]



def FreeSearch1(x):
    
    subvalue = ''
    i =''
    jokes = []
    freesearch = requests.get("https://api.chucknorris.io/jokes/search?query=" + x)
    freesearch_dict =  json.loads(freesearch.text)
    for key, value in freesearch_dict.items():    
        if key == "result":
            for subvalue in value:                
                for i in subvalue:
                    if i == "value":                        
                        #print(subvalue[i])
                        #print('*****')
                        jokes.append(subvalue[i])
    return jokes 
    
    

   
     
    
#print(All_Categories())
#Random_Joke()
#print(Catgory_Joke1("sport"))
#FreeSearch()
#list(FreeSearch1("bug"))
