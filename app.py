import os
from flask import Flask

"""
Create an instance of the class
"""
app = Flask(__name__)

@app.route("/") #Tell Flask what URL should trigger the following function.
def index():
    return "Hello, World"

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)