from flask import Flask

app = Flask(__name__)  # __name__ is just for referencing this file


@app.route('/')
def index():
    return "Hello this is my first Flask application"


if __name__ == "__main__":
    app.run(debug=True)
