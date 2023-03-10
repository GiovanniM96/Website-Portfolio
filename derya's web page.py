#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 18:46:28 2023

@author: giovanni
"""

from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    projects = [
        {
            "name": "Project 1",
            "description": "Description for project BLA BLA BLA BLA BLA BLA BLA BLA BLA BLA BLA BLA BLA BLA BLA BLA BLA BLA BLA BLA BLA BLA BLA BLA"
        },
        {
            "name": "Project 2",
            "description": "Description for project 2"
        },
        {
            "name": "Project 2",
            "description": "Description for project 2"
        }
    ]
    return render_template("projects.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True)
