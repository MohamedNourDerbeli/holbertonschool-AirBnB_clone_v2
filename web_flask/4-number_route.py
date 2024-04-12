#!/usr/bin/python3
"""Create a Flask application instance"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    This function handles requests to the root URL ("/").
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    This function handles requests to the "/hbnb" URL.
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    This function handles requests to the "/c/<text>" URL
    """
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python", defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """
    This function handles requests to the "/python/<text>" URL
    """
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    This function handles requests to the "/number/<n>" URL
    """
    return f"{n} is a number"


if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=5000)
