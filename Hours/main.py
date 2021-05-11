from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms import validators, SubmitField, StringField
import datasave

app = Flask("stundenblatt")

app.config["SECRET_KEY"] = "!1fabod2?"  # https://github.com/CarlosIUSalazar/Python-Flask-DatePicker #Why is this needed?


class MyForm(FlaskForm):   # create class to define what MyForm is - MyForm is based on FlaskForm
    chosen_date = DateField("Chosen Date", format="%Y-%m-%d", validators=(validators.DataRequired(),))  # format the DateField(WTForms) and set tha a validator is required otherwise error is given
    hours = StringField("Geben Sie ihre gearbeiteten Stunden ein:  ", validators=(validators.DataRequired(),))  # Create StringField for the hours, validator needed, currently getting an error if I put one here as well
    submit = SubmitField("Submit")  # variable for submit


@app.route("/", methods=["GET", "POST"])
def index():
    datum = MyForm()
    if datum.validate_on_submit():  # validiert ob submit durchgeführt wurde wurde
        datasave.zeit_erfassen(datum.chosen_date.data, datum.hours.data)  # call datasave program and give form.chosen_date

    return render_template("index.html", form=datum)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
