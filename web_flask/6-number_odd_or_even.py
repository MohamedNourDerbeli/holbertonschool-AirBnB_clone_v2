#!/usr/bin/python3
"""Create a Flask application instance"""
from flask import Flask
from flask import render_template


# Create a Flask application instance
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


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
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


@app.route("/number_template/<int:n>", strict_slashes=False)
def template_num(n):
    """
    This function handles requests to the "/number_template/<n>" URL
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    This function handles requests to the "number_odd_or_even/<n>" URL
    """
    if n % 2 == 0:
        result = "even"
    else:
        result = "odd"
    return render_template("6-number_odd_or_even.html\
", n=n, odd_or_even=result)


if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=5000)
