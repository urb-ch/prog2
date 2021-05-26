import json
from datetime import datetime
import calendar


def speichern(datei, hours, chosen_date):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[chosen_date] = hours

    # print(datei_inhalt)

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)
# def stunden_erfassen(stunden):
  # anzahl_stunden = stunden
  # print(anzahl_stunden)


def zeit_erfassen(datum, stunden):
    formatted_date = str(datum)
    correct_date = formatted_date  # currently transforming datum contents into string as DateForm is otherwise not possible to post in JSON format Object of type DateForm is not JSON serializable
    correct_hours = stunden  # should be given together with correct_date as individual parameter
    datei = "arbeitsstunden.json"
    speichern(datei, correct_hours, correct_date)
    ueberstunden(correct_hours, correct_date)
    # insights(correct_date)


def ausgabe_total():
    datei = "arbeitsstunden.json"
    try:
        with open(datei, "r") as open_file:  # opening datei in reading mode
            datei_inhalt = json.load(open_file)
            datei_inhalt = dict(sorted(datei_inhalt.items()))  # well can it be that easy to sort a dictionary?  Thank you mr. https://stackoverflow.com/questions/9001509/how-can-i-sort-a-dictionary-by-key
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt  # returning list


def ueberstunden(hours, chosen_date):
    ueberstunden_file = "ueberstunden.json"
    try:
        with open(ueberstunden_file) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[chosen_date] = round((hours - 8), 2)

    # print(datei_inhalt)

    with open(ueberstunden_file, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)

    # month_aggregation(datei_inhalt)

    # I would like to have an overview on which month I generated most overtime -> should I try and rearrange my dictionary for that to work with keys per month?


def ausgabe_overtime():  # https://www.dataquest.io/blog/python-datetime-tutorial/
    ueberstunden_file = "ueberstunden.json"
    try:
        with open(ueberstunden_file) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    # determine maximum amount of hours worked and associated key which is the date
    max_value = max(datei_inhalt.values())  # maximum value
    max_keys = [keys for keys, value in datei_inhalt.items() if value == max_value]
    max_keys = "".join(max_keys)

    # Form key into string format by using datetime
    datum = max_keys
    my_string = datum
    my_date = datetime.strptime(my_string, "%Y-%m-%d")
    string = (calendar.day_name[my_date.weekday()], " in ", calendar.month_name[my_date.weekday()])
    return_string = "".join(string)
    # print(max_value, max_keys)

    # determine sum of the total overtime
    sum_of_overtime = sum(datei_inhalt.values())
    # print(sum_of_overtime)

    # determine average of overtime
    avg_of_overtime = sum_of_overtime / len(datei_inhalt.values())
    avg_of_overtime = round(avg_of_overtime, 2)
    # print(avg_of_overtime)
    return sum_of_overtime, max_value, max_keys, avg_of_overtime, return_string

# def month_aggregation(dateiname):
#     keys = []
#     for key, value in dateiname.items():
#         a = key.split("-")
#         joined_keys = ["".join(a[0:2])]
#         hours = value
#         keys.append(joined_keys)
#     keys = list(set(keys))
#
#     for key in keys
#
#     # aggregation = {joined_keys:hours} # Neues Dictionary mit jahr und monat. Wenn key == key Summierte hours als values
#
#
# # def visualize():
#     # work on plotly to visualize over-/ undertime in a plot
