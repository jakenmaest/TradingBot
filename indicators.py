# Indicators are stored in a dictionary with the name as key, and 
# the function as the value. This can be called from a strategy either
# with or without parameters (must define defaults).

# TODO - move to constants file and enumerate
UPDATE_OPEN = 0
UPDATE_CLOSE = 1
UPDATE_SEC = 2
UPDATE_MIN = 3
UPDATE_HOUR = 4
UPDATE_DAY = 5

import pandas as pd
import pandas_ta as pta
from ta.trend import SMAIndicator, EMAIndicator, MACD
from ta.momentum import RSIIndicator
#from ta.volatility import *

## SETUP ##

#import ccxt
from Values import BYBIT_API_KEY, BYBIT_API_SECRET, OHLCV_DIR
#import Utilities as utils
#pd.set_option('display.max_rows', None)
# Switch Logging off and on
debugLog = True
#bybit = ccxt.bybit({'apiKey': BYBIT_API_KEY, 'secret': BYBIT_API_SECRET})

##############
# Indicators #
##############

def SimpleMovingAverage(data = pd.DataFrame, periods: int = 10, backtest: bool = False, verbose=debugLog):
    sma = SMAIndicator(data['close'], periods, False)
    return sma.sma_indicator()

def ExponentialMovingAverage(data = pd.DataFrame, periods: int = 10, backtest: bool = False, verbose=debugLog):
    ema = EMAIndicator(data['close'], periods, False)
    return ema.ema_indicator()

## REQUIRES TA-LIB
def TripleExponentialMovingAverage(data = pd.DataFrame, periods: int = 10, backtest: bool = False, verbose=debugLog):
    tema = pta.tema(close=data['close'], length=periods, talib=False)
    return tema

def RelativeStrengthIndex(data = pd.DataFrame, periods: int = 10, backtest: bool = False, verbose=debugLog):
    rsi = RSIIndicator(close=data['close'], window=periods, fillna=False)
    rsi_ = rsi.rsi()
    return rsi_

def MovingAverageConvergenceDivergence(data = pd.DataFrame, slow=26, fast=12, signal=9, backtest: bool = False, verbose=debugLog):
    macd = MACD(data['close'], fast, slow, signal, False)
    macd_ = macd.macd()
    signal_ = macd.macd_signal()
    diff_ = macd.macd_diff()
    return macd_, signal_, diff_

all_indicators = {
    ''' Indicators dictionary "name": <method call> '''
    'SMA': SimpleMovingAverage,
    'EMA': ExponentialMovingAverage,
    'TEMA': TripleExponentialMovingAverage,
    'RSI': RelativeStrengthIndex,
    'MACD': MovingAverageConvergenceDivergence
}
