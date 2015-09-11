import csv
from model import accident, car, place, user

FILES = {
    "place": "data/lieux.csv",
    "user": "data/usagers.csv",
    "carac": "data/caracteristiques.csv",
    "car": "data/vehicules.csv"
}

accidents = {}
line = 0

try:
    with open(FILES["carac"], encoding='ISO-8859-1') as f:
        reader = csv.DictReader(f)
        line = 1

        for row in reader:
            a = accident.Accident.fromRow(**row)
            if a is not None:
                accidents[a.Num_Acc] = a
            line += 1

    with open(FILES["place"], encoding='ISO-8859-1') as f:
        reader = csv.DictReader(f)
        line = 1

        for row in reader:
            a = place.Place(**row)
            if a.Num_Acc in accidents:
                accidents[a.Num_Acc].addPlace(a)
            line += 1

    with open(FILES["car"], encoding='ISO-8859-1') as f:
        reader = csv.DictReader(f)
        line = 1

        for row in reader:
            a = car.Car(**row)
            if a.Num_Acc in accidents:
                accidents[a.Num_Acc].addCar(a)
            line += 1
     
    with open(FILES["user"], encoding='ISO-8859-1') as f:
        reader = csv.DictReader(f)
        line = 1

        for row in reader:
            a = user.User(**row)
            if a.Num_Acc in accidents:
                accidents[a.Num_Acc].addUser(a)
            line += 1
except ValueError:
    print("Error at line " + str(line))
    raise


def get():
    return accidents




