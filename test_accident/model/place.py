from .util import Enum

class Place:

    def __init__(self, **kwargs):
        self.Num_Acc = kwargs["Num_Acc"]
        self.codr = kwargs["codr"] # TODO what is "codr"
        self.catr = Road.value(kwargs["catr"])
        self.voie = kwargs["voie"]
        self.v1 = kwargs["v1"]
        self.v2 = kwargs["v2"]
        self.circ = Way.value(kwargs["circ"])
        self.nbv = int(kwargs["nbv"]) if kwargs["nbv"] else -1
        self.pr = kwargs["pr"]
        self.pr1 = int(kwargs["pr1"]) if kwargs["pr1"] else -1
        self.vosp = Path.value(kwargs["vosp"])
        self.prof = Profile.value(kwargs["prof"])
        self.plan = Curve.value(kwargs["plan"])
        self.lartpc = int(kwargs["lartpc"]) if kwargs["lartpc"] else -1
        self.larrout = int(kwargs["larrout"]) if kwargs["larrout"] else -1
        self.surf = Condition.value(kwargs["surf"])
        self.infra = Infrastructure.value(kwargs["infra"])
        self.situ = Location.value(kwargs["situ"])
        self.env1 = kwargs["env1"]
        self.cars = {}

    def addCar(self, car):
        self.cars[car.letco] = car

    def isAllKnown(self):
        return self.circ != Way.UNKNOWN and \
            self.nbv != -1 and \
            self.vosp != Path.UNKNOWN and \
            self.prof != Profile.UNKNOWN and \
            self.plan != Curve.UNKNOWN and \
            self.surf != Condition.UNKNOWN and \
            self.infra != Infrastructure.UNKNOWN and \
            self.situ != Location.UNKNOWN

    def __repr__(self):
        return "Place \n" + \
            "\tNum_Acc : '" + self.Num_Acc + "'\n" + \
            "\tcodr : '" + self.codr + "'\n" + \
            "\tcatr : '" + self.catr.name + "'\n" + \
            "\tvoie : '" + self.voie + "'\n" + \
            "\tv1 : '" + self.v1 + "'\n" + \
            "\tv2 : '" + self.v2 + "'\n" + \
            "\tcirc : '" + self.circ.name + "'\n" + \
            "\tnbv : '" + str(self.nbv) + "'\n" + \
            "\tpr : '" + self.pr + "'\n" + \
            "\tpr1 : '" + str(self.pr1) + "'\n" + \
            "\tvosp : '" + self.vosp.name + "'\n" + \
            "\tprof : '" + self.prof.name + "'\n" + \
            "\tplan : '" + self.plan.name + "'\n" + \
            "\tlartpc : '" + str(self.lartpc) + "'\n" + \
            "\tlarrout : '" + str(self.larrout) + "'\n" + \
            "\tsurf : '" + self.surf.name + "'\n" + \
            "\tinfra : '" + self.infra.name + "'\n" + \
            "\tsitu : '" + self.situ.name + "'\n" + \
            "\tenv1 : '" + self.env1 + "'\n" + \
            "\tcars : '" + str(self.cars) + "'"

class Road(Enum):

    FREEWAY = 1
    HIGHWAY = 2
    SECONDARY = 3
    LOCAL = 4
    NOT_PUBLIC = 5
    PARKING_LOT = 6
    OTHER = 9

class Way(Enum):

    UNKNOWN = 0
    ONE = 1
    TWO = 2
    SEPARATED = 3
    VARIABLE = 4

class Path(Enum):

    UNKNOWN = 0
    BICYCLE = 1
    BANK = 2 # TODO figure out 'Banque cyclable' meaning
    RESERVED = 3

class Profile(Enum):

    UNKNOWN = 0
    FLAT = 1
    HILL = 2
    TOP = 3
    BOTTOM = 4

class Curve(Enum):

    UNKNOWN = 0
    STRAIGHT = 1
    LEFT = 2
    RIGHT = 3
    S = 4

class Condition(Enum):

    UNKNOWN = 0
    USUAL = 1
    WET = 2
    PUDDLE = 3
    FLOODED = 4
    SNOW = 5
    MUD = 6
    ICY = 7
    OIL = 8
    OTHER = 9

class Infrastructure(Enum):

    UNKNOWN = 0
    TUNNEL = 1
    BRIDGE = 2
    INTERCHANGE = 3
    RAILWAY = 4
    CIRCLE = 5
    PEDESTRIAN = 6
    TOLL = 7

class Location(Enum):

    UNKNOWN = 0
    PAVEMENT = 1
    EMERGENCY_LANE = 2
    SHOULDER = 3
    SIDEWALK = 4
    BICYCLE_PATH = 5
