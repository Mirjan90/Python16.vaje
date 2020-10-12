import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name="Mirjan"
    cities = ["Ljubljana", "Maribor", "Vienna"]
    year = datetime.datetime.now().year
    menu = [
        {
            "text": "Home",
            "link": "/"
        },
        {
            "text": "ABOUT ME",
            "link": "About me"
        }
            ]
    return render_template("index.html", name=name, cities=cities, menu=menu)

@ app.route('/about')
def about():
        return render_template("about.html")

if __name__== '__main__':
    app.run()