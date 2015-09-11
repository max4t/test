from .util import Enum

class Accident:
    
    def __init__(self, **kwargs):
        self.Num_Acc = kwargs["Num_Acc"]
        self.jour = int(kwargs["jour"])
        self.mois = int(kwargs["mois"])
        self.an = int(kwargs["an"]) 
        if not kwargs["hrmn"]:
            raise ValueError("empty string")
        self.hrmn = (int(kwargs["hrmn"][:-2] or 0), int(kwargs["hrmn"][-2:]))
        self.lum = Light.value(kwargs["lum"])
        self.dep = kwargs["dep"]
        self.com = kwargs["com"]
        self.agg = CitySize.value(kwargs["agg"])
        self.int = Intersection.value(kwargs["int"])
        self.atm = Weather.value(kwargs["atm"])
        self.col = Collision.value(kwargs["col"])
        self.adr = kwargs["adr"]
        self.gps = Area.value(kwargs["gps"])
        self.lat = float(kwargs["lat"])
        self.long = float(kwargs["long"])
        self.places = {}
        self.cars = {}
        self.users = []

    def addCar(self, car):
        self.places[car.codr].addCar(car)
        self.cars[car.letco] = car

    def addPlace(self, place):
        self.places[place.codr] = place

    def addUser(self, user):
        self.cars[user.letco].addUser(user)
        self.users.append(user)

    def isAllKnown(self):
        for key in self.places:
            if not self.places[key].isAllKnown():
                print(str(self.places[key]))
                return False
        for key in self.cars:
            if not self.cars[key].isAllKnown():
                print(self.cars[key])
                return False
        for user in self.users:
            print(user)
            if not user.isAllKnown():
                return False
        return True

    @classmethod
    def fromRow(cls, **kwargs):
        try:
            float(kwargs["long"])
        except ValueError:
            return None
        if not kwargs["lat"] or not kwargs["long"]:
            return None
        return cls(**kwargs)


class Light(Enum):

    DAY = 1
    TWILIGHT_DAWN = 2
    NIGHT_NO_LIGHT = 3
    NIGHT_LIGHT_ON = 4
    NIGHT_LIGHT_OFF = 5

class CitySize(Enum):

    OUTSIDE = 1
    UNDER_2M = 2
    BETWEEN_2M_5M = 3
    BETWEEN_5M_10M = 4
    BETWEEN_10M_20M = 5
    BETWEEN_20M_50M = 6
    BETWEEN_50M_100M = 7
    BETWEEN_100M_300M = 8
    OVER_300M = 9

class Intersection(Enum):

    NONE = 1
    TYPE_X = 2
    TYPE_T = 3
    TYPE_Y = 4
    TYPE_4 = 5
    CIRCLE = 6
    SQUARE = 7
    CROSSING = 8
    OTHER = 9

class Weather(Enum):

    REGULAR = 1
    SHOWER_RAIN = 2
    DRIVING_RAIN = 3
    SNOW = 4
    FOG = 5
    HIGH_WIND = 6
    BLINDING = 7
    OVERCAST = 8
    OTHER = 9

class Collision(Enum):

    HEAD_ON_2 = 1
    IN_THE_BACK_2 = 2
    BY_SIDE_2 = 3
    MORE_CHAINED = 4
    MORE_MULTIPLE = 5
    OTHER = 6
    NONE = 7

class Area(Enum):

    UNKNOWN = ""
    METROPOLE = "M"
    ANTILLES = "A"
    GUYANE = "G"
    REUNION = "R"
    MAYOTTE = "Y"

    @classmethod
    def value(cls, v):
        return cls(v)

