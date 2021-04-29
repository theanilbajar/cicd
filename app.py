import os
from flask import Flask, render_template
from buzz import generator
from comic import xkcd_app

app = Flask(__name__, template_folder='./comic/templates')

@app.route("/")
# def home_page():
#     return '<html><body><a href="/xkcd">Random XKCD Comic</a></body></html>'

# @app.route("")
def xkcd_comic():
    xkcd_data = xkcd_app.getRandomXkcdImage()
    if xkcd_data is None:
        return '<html><body><a href="/xkcd">Random XKCD Comic</a></body></html>'
    else:
        return render_template("index.html", data=xkcd_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))