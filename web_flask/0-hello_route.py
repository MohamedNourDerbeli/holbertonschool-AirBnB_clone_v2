#!/usr/bin/python3
"""Create a Flask application instance"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Return a friendly greeting."""
    return "Hello HBNB!"


if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=5000)
