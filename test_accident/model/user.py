from .util import Enum

class User:

    def __init__(self, **kwargs):
        self.Num_Acc = kwargs["Num_Acc"]
        self.letco = kwargs["letco"]
        self.place = Sit.value(kwargs["place"])
        self.catu = Category.value(kwargs["catu"])
        self.grav = Injury.value(kwargs["grav"])
        self.sexe = Gender.value(kwargs["sexe"])
        self.trajet = Ride.value(kwargs["trajet"])
        self.secu = Safety.value(kwargs["secu"])
        self.locp = Location.value(kwargs["locp"])
        self.actp = Action.value(kwargs["actp"])
        self.etatp = Pedestrian.value(kwargs["etatp"])
        self.an_nais = int(kwargs["an_nais"]) if kwargs["an_nais"] else -1

    def isAllKnown(self):
        return self.an_nais != -1 and \
            self.place != Sit.UNKNOWN and \
            self.trajet != Ride.UNKNOWN and \
            self.secu != Safety.INST[None][None] and \
            self.locp != Location.UNKNWON and \
            self.actp != Action.UNKNWON and \
            self.etatp != Pedestrian.UNKNWON

class Sit(Enum):

    UNKNOWN = 0
    DRIVER = 1
    PASSENGER = 2
    MIDDLE_FRONT = 6
    DRIVER_BACK_SIT = 4
    PASSENGER_BACK_SIT = 3
    MIDDLE_BACK_SIT = 5
    DRIVER_MIDDLE_SIT = 7
    PASSENGER_MIDDLE_SIT = 9
    MIDDLE_MIDDLE_SIT = 8

    MOTO_DRIVER = 1
    MOTO_PASSENGER = 2
    MOTO_SIDECAR = 3

class Category(Enum):

    DRIVER = 1
    PASSENGER = 2
    PEDESTRIAN = 3
    PEDESTRIAN_ROLLER = 4

class Gender(Enum):

    MALE = 1
    FEMALE = 2

class Ride(Enum):

    UNKNOWN = 0
    HOME_WORK = 1
    HOME_SCHOOL = 2
    ERRANDS = 3
    BUSINESS = 4
    HOBBY = 5
    OTHER = 9

class Safety:

    INST = {}

    class Type(Enum):

        BELT = 1
        HELMET = 2
        CHILD_SAFETY = 3
        REFLECTIVE = 4
        OTHER = 9

    class Use(Enum):

        YES = 1
        NO = 2
        UNKNOWN = 3

    @classmethod
    def value(cls, value):
        t = cls.Type.value(value[0]) if len(value) > 1 else None
        u = cls.Use.value(value[1]) if len(value) > 2 else None
        if t not in cls.INST:
            cls.INST[t] = {}
        if u not in cls.INST[t]:
            cls.INST[t][u] = cls(t, u)
        return cls.INST[t][u]

    def __init__(self, typ, use):
        self.type = typ
        self.use = use

class Location(Enum):

    UNKNOWN = 0
    OVER_50M_FROM_CROSSWALK = 1
    UNDER_50M_FROM_CROSSWALK = 2
    WITHOUT_INDICATOR = 3
    WITH_INDICATOR = 4
    SIDEWALK = 5
    SHOULDER = 6
    SHELTER = 7
    SIDE_PATH = 8

class Action(Enum):

    UNKNOWN = 0
    BUMPING_CAR_WAY = 1
    REVERSE_BUMPING_CAR_WAY = 2
    CROSSING = 3
    HIDDEN = 4
    RUNNING = 5
    WITH_ANIMAL = 6
    OTHER = 9

class Injury(Enum):

    SAFE = 1
    DEAD = 2
    HOSPITALIZED = 3
    SLIGTHLY_INJURED = 4

class Pedestrian(Enum):

    UNKNOWN = 0
    ALONE = 1
    WITH_COMPANY = 2
    GROUP = 3

