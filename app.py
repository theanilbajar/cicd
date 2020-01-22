import os

from flask import Flask
from buzz import generator
from comic import xkcd_app

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
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))