import json
from datetime import datetime
import calendar

# as I am using the same file multiple times I opt to open it per function to circumvent accidental overwrites.

def zeit_erfassen(datum, stunden):
    formatted_date = str(datum)
    correct_date = formatted_date  # currently transforming datum contents into string as DateForm is otherwise not possible to post in JSON format Object of type DateForm is not JSON serializable
    correct_hours = stunden  # should be given together with correct_date as individual parameter
    datei = "arbeitsstunden.json"
    speichern(datei, correct_hours, correct_date)
    ueberstunden(correct_hours, correct_date)


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

def ausgabe_total():
    datei = "arbeitsstunden.json"
    try:
        with open(datei, "r") as open_file:  # opening datei in reading mode
            datei_inhalt = json.load(open_file)
            datei_inhalt = dict(sorted(datei_inhalt.items()))  # well can it be that easy to sort a dictionary?  Thank you mr. https://stackoverflow.com/questions/9001509/how-can-i-sort-a-dictionary-by-key
    except FileNotFoundError:
        datei_inhalt = {}

    # determine sum of the total time worked
    sum_of_hours = sum(datei_inhalt.values())


    return datei_inhalt, sum_of_hours # returning list


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

    # I would like to have an overview on which month I generated most overtime -> should I try and rearrange my dictionary for that to work with keys per month?


def ausgabe_overtime():  # https://www.dataquest.io/blog/python-datetime-tutorial/
    ueberstunden_file = "ueberstunden.json"
    try:
        with open(ueberstunden_file) as open_file:
            datei_inhalt = json.load(open_file)
            datei_inhalt = dict(sorted(datei_inhalt.items()))
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
    return sum_of_overtime, max_value, max_keys, avg_of_overtime, return_string, datei_inhalt

def monthly_aggregation():
    datei = "arbeitsstunden.json"
    try:
        with open(datei, "r") as open_file:  # opening datei in reading mode
            datei_inhalt = json.load(open_file)
            datei_inhalt = dict(sorted(datei_inhalt.items()))
    except FileNotFoundError:
        datei_inhalt = {}
    original_dict = datei_inhalt

    # First approach to collect monthly data - changed it to aggregating in a dictionary as it is a cleaner way rather than using the same functio over and over again
    # year_2021 = "2021"
    # january="2021-01"
    # february="2021-02"
    # march="2021-03"
    # april="2021-04"
    # may="2021-05"
    # june="2021-06"
    # july="2021-07"
    # august="2021-09"
    # september="2021-10"
    # october="2021-10"
    # november="2021-11"
    # december="2021-12"
    #
    # #work further on this and print all values from testdict that containt the value string from year
    # print("The original dictionary is: " + str(test_dict))
    #
    # res_jan = [val for key, val in test_dict.items() if january in key]
    # res_jan = sum(res_jan)
    #
    # res_feb = [val for key, val in test_dict.items() if february in key]
    # res_feb = sum(res_feb)
    #
    # res_mar = [val for key, val in test_dict.items() if march in key]
    # res_mar = sum(res_mar)
    #
    # res_apr = [val for key, val in test_dict.items() if april in key]
    # res_apr = sum(res_apr)
    #
    # res_may = [val for key, val in test_dict.items() if may in key]
    # res_may = sum(res_may)
    #
    # res_jun = [val for key, val in test_dict.items() if june in key]
    # res_jun = sum(res_jun)
    #
    # res_jul = [val for key, val in test_dict.items() if july in key]
    # res_jul = sum(res_jul)
    #
    # res_aug = [val for key, val in test_dict.items() if august in key]
    # res_aug = sum(res_aug)
    #
    # res_sep = [val for key, val in test_dict.items() if september in key]
    # res_sep = sum(res_sep)
    #
    # res_oct = [val for key, val in test_dict.items() if october in key]
    # res_oct = sum(res_oct)
    #
    # res_nov = [val for key, val in test_dict.items() if november in key]
    # res_nov = sum(res_nov)
    #
    # res_dec = [val for key, val in test_dict.items() if december in key]
    # res_dec = sum(res_dec)
    #
    # res_year_2021 = [val for key, val in test_dict.items() if year_2021 in key]
    # sum_res_year_2021 = sum(res_year_2021)
    # return res_jan, res_feb, res_mar, res_apr, res_may, res_jun, res_jul, res_aug, res_sep, res_oct, res_nov, res_dec, sum_res_year_2021,

    # setting up an empty dictionary where data from original dict will be filled in
    result_dict = {"2021-01": 0.00, "2021-02": 0.00, "2021-03": 0.00, "2021-04": 0.00, "2021-05": 0.00, "2021-06": 0.00,
                   "2021-07": 0.00, "2021-08": 0.00, "2021-09":0.00, "2021-10":0.00, "2021-11":0.00, "2021-12":0.00}
    #print("The original dictionary is: " + str(test_dict))
    #print("The original dictionary is: " + str(result_dict))
    for month in result_dict:
        month_dict = {key: value for key, value in original_dict.items() if key.startswith(month)} # creating an additional month dictionary. key is key from original dict but restricted to month(key) from result dict. startswith helps match the keys from original_dict file to result_dict
        result_dict[month] = sum(month_dict.values()) #adding sum from month_dict values to associated key from result dict
    #print(result_dict)
    result_dict['2021'] = sum(result_dict.values()) #creating a new key in result dict "2021" with sum of all values as value
    #print(result_dict)

    # returning dict as list
    return list(result_dict.values())