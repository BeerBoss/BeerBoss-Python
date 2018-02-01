from enum import Enum


# States are inverted because of the bidirectional level shifter
class RelayState(Enum):
    OFF = True
    ON = False


class Action(Enum):
    COOL = [RelayState.ON, RelayState.OFF]
    HEAT = [RelayState.OFF, RelayState.ON]
    NOTHING = [RelayState.OFF, RelayState.OFF]
