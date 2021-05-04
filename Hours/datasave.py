import json



def speichern(datei, chosen_date):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt["Datum"] = chosen_date

    print(datei_inhalt)

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)



def zeit_erfassen(datum):
    string_date = str(datum)
    print(string_date)
    correct_date = string_date[79:90] #ask teacher how I get the bloody Data only
    x = {"Datum": correct_date} #currently transforming datum contents into string as DateForm is otherwise not possible to post in JSON format Object of type DateForm is not JSON serializable
    datei = "datasave.json"
    speichern(datei, x)
