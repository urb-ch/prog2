import json



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
  #  anzahl_stunden = stunden
  #  print(anzahl_stunden)


def zeit_erfassen(datum, stunden):
    formatted_date = str(datum)
    correct_date = formatted_date # currently transforming datum contents into string as DateForm is otherwise not possible to post in JSON format Object of type DateForm is not JSON serializable
    correct_hours = stunden  # should be given together with correct_date as individual parameter
    datei = "datasave.json"
    speichern(datei, correct_hours, correct_date)
