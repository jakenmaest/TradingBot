##
## UTILITIES CLASS
##

import pandas as pd
from enum import Enum
#import OHLCV

class CandleStatus(Enum):
    # States
    VALID=1
    NULL=0
    ERROR=-1
    # Error States
    INVALID_TIMESTAMP=-2
    TIME_SKIP_FWD=-3
    TIME_SKIP_BACK=-4
    HIGH_TOO_LOW=-5
    LOW_TOO_HIGH=-6
    OPEN_ERROR_LOW=-7
    OPEN_ERROR_HIGH=-8
    CLOSE_LOW=-9
    CLOSE_HIGH=-10
    INVALID_VOLUME=-11
    MISSING_DATA=-12

## CHECK CANDLES CLASS
#       Class for checking the validity of a set of candles, including 
#       out of order candles, highs lower than lows etc., and makes sure
#       the data is clean for full ohlcv use
# TODO: Split into utils class for global use
#def CheckOHLCV(candles: OHLCV) -> pd.DataFrame: pass
        # check timestamp synchnicity
        # check candle values are valid
        # is low higher than high
        # is high lower than low
        # is open too high or low
        # is close too high or low
        # is the volume accurate

def DifferencePercent(num1, num2):
    '''returns ( (num2 - num1) / num1) * 100'''
    return((num2-num1)/num1)*100

def DifferenceValue(num1, num2):
    '''returns num2 - num1'''
    return num2-num1

class Utilities():
    pass
