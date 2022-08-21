from enum import Enum

class Ocean(Enum):
    PACIFIC = 1
    ATLANTIC = 2
    INDIAN = 3
    ARCTIC = 4
    SOUTHERN = 5

class Unit(Enum):
    Fahrenheit= 1
    Celsius = 2
    Kelvin = 3
    Rankine = 4
    Newton = 5
    Romer = 6
    Reaumur = 7
    Delisle = 8
    
class DateFormat(Enum):
    DMY = '%d/%m/%Y %H:%M:%S'
    YMD	 = '%Y/%m/%d %H:%M:%S'
    MDY = '%m/%d/%Y %H:%M:%S'