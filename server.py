from flask import Flask
from api import register
from strip import setup

if __name__ == '__main__':
    app = Flask(__name__)
    setup({})
    register(app)
    app.run(port=8080, host="0.0.0.0")
