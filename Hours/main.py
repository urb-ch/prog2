from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms import validators, SubmitField
import datasave

app = Flask("stundenblatt")

app.config["SECRET_KEY"] = "!1alpaka2?"


class DateForm(FlaskForm): #create class for DateForm
    chosen_date = DateField("Chosen Date", format="%Y-%m-%d", validators=(validators.DataRequired(),)) #format the DateField and set a validator
    submit = SubmitField("Submit") #variable for submit


@app.route("/", methods=["GET", "POST"])
def index():
    form = DateForm()
    if form.validate_on_submit(): #validiert ob submit durchgeführt wurde wurde
        datasave.zeit_erfassen(form.chosen_date) #call datasave program and give form.chosen_date


    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
