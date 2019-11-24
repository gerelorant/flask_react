from flask import Flask
from flask_react import React


app = Flask(__name__)
react = React(
    app,
    extensions=("material", "components"),
    jsx_folder='static/react/jsx/'
)


if __name__ == '__main__':
    app.run()
