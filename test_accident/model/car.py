from .util import Enum

class Car:

    def __init__(self, **kwargs):
        self.Num_Acc = kwargs["Num_Acc"]
        self.letco = kwargs["letco"]
        self.codr = kwargs["codr"]
        self.senc = Direction.value(kwargs["senc"])
        self.catv = Category.value(kwargs["catv"])
        self.occutc = int(kwargs["occutc"])
        self.obs = Obstacle.value(kwargs["obs"])
        self.obsm = MovingObstacle.value(kwargs["obsm"])
        self.choc = Impact.value(kwargs["choc"])
        self.manv = Maneuver.value(kwargs["manv"])
        self.users = []

    def addUser(self, user):
        self.users.append(user)

    def isAllKnown(self):
        return self.senc != Direction.UNKNOWN and \
            self.obs != Obstacle.UNKNOWN and \
            self.obsm != Obstacle.UNKNOWN and \
            self.choc != Impact.UNKNOWN and \
            self.manv != Maneuver.UNKNOWN

class Direction(Enum):

    UNKNOWN = 0
    ASC = 1
    DESC = 2

class Category(Enum):

    # 01 - Bicyclette
    BICYCLE = 1
    # 02 - Cyclomoteur <50cm3
    MOPED = 2
    # 03 - Voiturette (Quadricycle à moteur carrossé) (anciennement "voiturette ou tricycle à moteur")
    SMALL_CAR = 3
    # 04 - Référence plus utilisée depuis 2006 (scooter immatriculé)
    UNUSED_SCOOTER = 4
    # 05 - Référence plus utilisée depuis 2006 (motocyclette)
    UNUSED_MOTORBIKE = 5
    # 06 - Référence plus utilisée depuis 2006 (side-car)
    UNUSED_SIDECAR = 6
    # 07 - VL seul
    CAR = 7
    # 08 - Catégorie plus utilisée (VL + caravane)
    CAR_CARAVAN = 8
    # 09 - Catégorie plus utilisée (VL + remorque)
    CAR_TRAILER = 9
    # 10 - VU seul 1,5T <= PTAC <= 3,5T avec ou sans remorque (anciennement VU seul 1,5T <= PTAC <= 3,5T)
    HEAVY_CAR = 10
    # 11 - Référence plus utilisée depuis 2006 (VU (10) + caravane)
    UNUSED_HEAVY_CAR_CARAVAN = 11
    # 12 - Référence plus utilisée depuis 2006 (VU (10) + remorque)
    UNUSED_HEAVY_CAR_TRAILER = 12
    # 13 - PL seul 3,5T <PTCA <= 7,5T
    LIGHT_TRUCK = 13
    # 14 - PL seul > 7,5T
    MEDIUM_TRUCK = 14
    # 15 - PL > 3,5T + remorque
    HEAVY_TRUCK = 15
    # 16 - Tracteur routier seul
    TRACTOR = 16
    # 17 - Tracteur routier + semi-remorque
    TRACTOR_SEMI = 17
    # 18 - Référence plus utilisée depuis 2006 (transport en commun)
    UNUSED_PUBLIC_TRANSPORT = 18
    # 19 - Référence plus utilisée depuis 2006 (tramway)
    UNUSED_STREETCAR = 19
    # 20 - Engin spécial
    SPECIAL = 20
    # 21 - Tracteur agricole
    FARMING_TRACTOR = 21
    # 30 - Scooter < 50 cm3
    LIGHT_SCOOTER = 30
    # 31 - Motocyclette > 50 cm et <= 125 cm
    MEDIUM_MOTORBIKE = 31
    # 32 - Scooter >50cm et<=125cm
    MEDIUM_SCOOTER = 32
    # 33 - Motocyclette > 125 cm
    HEAVY_MOTORBIKE = 33
    # 34 - Scooter > 125 cm
    HEAVY_SCOOTER = 34
    # 35 - Quad léger <= 50 cm (Quadricycle à moteur non carrossé)
    SMALL_QUAD = 35
    # 36 - Quad lourd > 50 cm (Quadricycle à moteur non carrossé)
    HEAVY_QUAD = 36
    # 37 - Autobus
    BUS = 37
    # 38 - Autocar
    COACH = 38
    # 39 - Train
    TRAIN = 39
    # 40 - Tramway
    STREETCAR = 40
    # 99 - Autre véhicule
    OTHER = 99

class Obstacle(Enum):

    UNKNOWN = 0
    PARKED_CAR = 1
    TREE = 2
    METAL_BARRIER = 3
    CONCRETE_BARRIER = 4
    OTHER_BARRIER = 5
    WALL = 6
    TRAFFIC_FRAME = 7
    POLE = 8
    STREET_FURNITURE = 9
    PARAPET = 10
    SHELTER = 11
    SIDEWALK = 12
    DITCH = 13
    PAVEMENT_OBSTACLE = 14
    SIDEWALK_OBSTACLE = 15
    NO_OBSTACLE = 16

class MovingObstacle(Enum):

    UNKNOWN = 0
    PEDESTRIAN = 1
    VEHICULE = 2
    RAIL_VEHICULE = 4
    PET = 5
    WILD_ANIMAL = 6
    OTHER = 9

class Impact(Enum):

    UNKNOWN = 0
    FRONT = 1
    FRONT_RIGHT = 2
    FRONT_LEFT = 3
    BACK = 4
    BACK_RIGHT = 5
    BACK_LEFT = 6
    SIDE_RIGHT = 7
    SIDE_LEFT = 8
    MULTIPLE = 9

class Maneuver(Enum):

    UNKNOWN = 0
    # Before
    NO_CHANGE_DIRECTION = 1
    SAME_WAY_LANE = 2
    BETWEEN_LANES = 3
    IN_REVERSE = 4
    WRONG_WAY = 5
    THROUGH_MEDIAN_STRIP = 6
    BUS_LANE_SAME_WAY = 7
    BUS_LANE_REVERSE_WAY = 8
    EASING_INTO = 9
    TURNING_AROUND = 10
    # change lane
    CHANGE_LANE_TO_LEFT = 11
    CHANGE_LANE_TO_RIGHT = 12
    # drift
    DRIFT_LEFT = 13
    DRIFT_RIGHT = 14
    # turn
    TURN_LEFT = 15
    TURN_RIGHT = 16
    # overtake
    OVERTAKE_LEFT = 17
    OVERTAKE_RIGHT = 18
    # misc
    CROSS_PAVEMENT = 19
    PARK_MANEUVER = 20
    EVASION_MANEUVER = 21
    OPEN_DOOR = 22
    STOPPED_NOT_PARKED = 23
    PARKED_WITH_PASSENGERS = 24

