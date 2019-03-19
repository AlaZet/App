from flask import Flask, render_template

app = Flask(__name__)

LINKS = [
    {
        "url": "https://www.airhelp.com",
        "title": "AirHelp"
    },
    {
        "url": "https://bitbucket.org/",
        "title": "BB"
    }
]

@app.route("/")
def hello():
    return render_template("index.html", links=LINKS)

if __name__ == "__main__":
    app.run()