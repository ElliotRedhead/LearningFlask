import os
import json
from flask import Flask, render_template

"""
Create an instance of the class
"""
app = Flask(__name__)

@app.route("/") #Tell Flask what URL should trigger the following function.
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    data = []
    with open("data/company.json","r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title = "About", company=data)

@app.route("/contact")
def contact():
    return render_template("contact.html", page_title = "Contact")

@app.route("/careers")
def careers():
    return render_template("careers.html", page_title = "Careers")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)