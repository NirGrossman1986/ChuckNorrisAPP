#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 13:18:23 2021

@author: nir
"""
from flask import Flask, render_template, request
from ChuckNorrisJokes import Random_Joke, Catgory_Joke1, FreeSearch1

def joke():
    joke = Random_Joke()
    processed_text = joke
    # Some internal stuff with processed text
    return processed_text

#joke()
#x = "sport"    
#print(Catgory_Joke1("sport"))





print(FreeSearch1("bug"))

                    











