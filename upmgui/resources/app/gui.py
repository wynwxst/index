import sys
import os
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/search/")
def search():
    query = request.args.get('query')
    if query == None:
        query = ""
    return render_template("search.html",query=query)
@app.route("/sources/")
def sources():
    return render_template("sources.html")
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
