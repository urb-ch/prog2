from datetime import datetime
import json


def speichern(datei, key, value):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = value

    # print(datei_inhalt)

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)


def zeit_erfassen(stunden):
    datei_name = "datasave.json"
    zeitpunkt = datetime.now()
    speichern(datei_name, zeitpunkt, stunden)
    return zeitpunkt, stunden