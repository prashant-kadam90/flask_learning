#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:12:14 2024

@author: prashantkadam
"""

from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/")
def index():
    return render_template("page1.html")

    # Handle button press
@app.route("/handle_button", methods=["POST"])
def handle_button():
    button_value = request.form.get("button")
    return f"You clicked the button! Value received: {button_value}"

if __name__ == "__main__":
    app.run(debug=True)
    