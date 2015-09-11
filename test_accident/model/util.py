import enum

class Enum(enum.Enum):

    @classmethod
    def value(cls, v):
        return cls(int(v or 0))

