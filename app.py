# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html")


if __name__ == "__main__":
    print "-----------------------------------------< levibracken.com >----"
    app.run(debug=True) # If running directly from the CLI, run in debug mode.   