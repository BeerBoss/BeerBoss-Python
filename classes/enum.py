from enum import Enum


class RelayState(Enum):
    OFF = False
    ON = True

class Action(Enum):
    COOL = [RelayState.ON, RelayState.OFF]
    HEAT = [RelayState.OFF, RelayState.ON]
    NOTHING = [RelayState.OFF, RelayState.OFF]
