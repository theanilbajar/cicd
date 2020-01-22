import os

from flask import Flask
from buzz import generator
from comic import xkcd_app

HOST = "0.0.0.0"
PORT = int(os.getenv('PORT', 5000))

app = Flask(__name__)

@app.route("/")
def home_page():
    page = '<html><body>'
    page += '<a href="/xkcd">Random XKCD Comic</a>'
    page += '</body></html>'
    return page

@app.route("/xkcd/")
def xkcd_comic():
    page = '<html><body>'
    page += '<img src="'+xkcd_app.getRandomXkcdImage()+'" style="margin: auto;"/>'
    page += '</body></html>'
    return page


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)