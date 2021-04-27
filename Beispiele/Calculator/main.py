from flask import Flask
from flask import render_template
from flask import request

app = Flask("taschenrechner")


@app.route("/taschenrechner/", methods=["GET", "POST"])  # approute for URL is calculator
def rechner():  # what should be returned
    if request.method == "POST":
        zahl1 = request.form["erste_zahl"]
        zahl2 = request.form["zweite_zahl"]
        zahl3 = request.form["dritte_zahl"]
        summe = int(zahl1) + int(zahl2) + int(zahl3)
        ergebnis = "Das Ergebnis ist " + str(summe)
        return ergebnis

    return render_template("taschenrechner.html")


if __name__ == "__main__":  # Tell python to run the program with the following parameters - Always has to be named main!
    app.run(debug=True, port=5000)
