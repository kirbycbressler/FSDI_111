#!/usr/bin/env python3
#-*- coding: utf8 -*-
"""simple flask app"""

from flask import Flask

app = Flask(__name__)  #__name__ is a magic variable or dunder variable 


@app.route("/")
def about_me():     #view function
  me = {
    "first_name": "Kirby",
    "last_name": "Bressler",
    "hobbies": "Art",
    "test": True
  }
  return me



