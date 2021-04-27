from flask import Flask
from flask import render_template
from flask import request
import datasave

app = Flask("stundenblatt")

@app.route('/')
def index():
    return "Herzlich willkommen zum Arbeitszeiterfassungssystem"

@app.route("/erfassen/", methods=['GET', 'POST'])
def zeit_erfassen():
    if request.method == 'POST':
        stunden = request.form['stunden']
        zeitpunkt, stunden = datasave.zeit_erfassen(stunden)
        rueckgabe_string = "Gespeichert: " + stunden + " um " + str(zeitpunkt)
        return rueckgabe_string


    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)