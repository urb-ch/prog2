from flask import Flask
from flask import render_template
import json

app = Flask("jinja")


@app.route("/jinja/", methods=['GET', 'POST'])
def jinja():
    dinger = ["Eins", "Zwei", "Drei", "4"]

    return render_template("index.html", dinger=dinger, zahl= 3)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
