from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms import validators, SubmitField, FloatField  # using wtforms because I need validators and a datefield
import plotly.express as px
from plotly.offline import plot
import datasave

app = Flask("stundenblatt")

app.config["SECRET_KEY"] = "!1fabod2?"  # https://github.com/CarlosIUSalazar/Python-Flask-DatePicker WTForms will use the SECRET_KEY as a salt to create a CSRF token. The csrf_token is generated automatically by the WTForms and it changes each time the page is rendered. This helps us to protect our site against CSRF attacks.


class MyForm(FlaskForm):   # create class to define what MyForm is - MyForm is based on FlaskForm objektorientert darum class. Wird genutzt um die validierung durch submit für die ganze Klasse durchzuführen.
    chosen_date = DateField("Please choose a date", format="%Y-%m-%d", validators=(validators.DataRequired(),))  # format the DateField(WTForms) and set a validator. this is required otherwise error is given
    hours = FloatField("Enter the amount of worked hours:  ", validators=(validators.DataRequired(),))  # Create StringField for the hours, validator needed, currently getting an error if I put one here as well
    submit = SubmitField("Submit")  # variable for submit


@app.route("/home", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/submission", methods=["GET", "POST"])
def erfassen():
    form_data = MyForm()  # instanzierung der klasse
    # confirmation_date = str(form_data.chosen_date.data)
    # confirmation_hours = str(form_data.hours.data)
    # confirmation_string = "You have worked " + confirmation_hours + " hours on the " + confirmation_date
    if form_data.validate_on_submit():  # validiert ob submit durchgeführt wurde wurde
        datasave.zeit_erfassen(form_data.chosen_date.data, form_data.hours.data)  # call datasave program and give form.chosen_date

    return render_template("erfassen.html", form=form_data)


@app.route("/overview", methods=["GET", "POST"])
def Day_by_Day():
    if request.method == "GET":
        datasave.ausgabe_total()
    daten = datasave.ausgabe_total()
    return render_template("day_by_day.html", data=daten[0])  # returning data to call it via jinja later


@app.route("/insights", methods=["GET", "POST"])
def insights():
    if request.method == "GET":
        datasave.ausgabe_overtime()
        datasave.ausgabe_total()
    # plotly bar plot to visualize accumulated overtime
    working_hours_data = datasave.ausgabe_total()
    overtime_data = datasave.ausgabe_overtime()
    monthly_data = datasave.monthly_aggregation()
    fig = px.bar(x=overtime_data[5].keys(), y=overtime_data[5].values(),
    labels = {
                 "x" : "Date",
                 "y" : "Amount of Overtime",
             },
             title = "Overtime per Date"
    )
    div = plot(fig, output_type="div")
    return render_template("insights.html", overtimedata=overtime_data, viz_div=div, totaltime=working_hours_data, monthtime=monthly_data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
