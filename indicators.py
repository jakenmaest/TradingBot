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

import enum
import pandas as pd
import pandas_ta as pta
from ta.trend import SMAIndicator, EMAIndicator, MACD
from ta.momentum import RSIIndicator
from ta.momentum import AwesomeOscillatorIndicator as AweOsc
from ta.volatility import BollingerBands as BollBands
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

def SimpleMovingAverage(data = pd.DataFrame, periods: int = 9, backtest: bool = False, verbose=debugLog):
    sma = SMAIndicator(data['close'], periods, False)
    return sma.sma_indicator()

def ExponentialMovingAverage(data = pd.DataFrame, periods: int = 9, backtest: bool = False, verbose=debugLog):
    ema = EMAIndicator(data['close'], periods, False)
    return ema.ema_indicator()

## REQUIRES TA-LIB
def TripleExponentialMovingAverage(data = pd.DataFrame, periods: int = 9, backtest: bool = False, verbose=debugLog):
    tema = pta.tema(close=data['close'], length=periods, talib=False)
    return tema

def RelativeStrengthIndex(data = pd.DataFrame, periods: int = 10, backtest: bool = False, verbose=debugLog):
    rsi = RSIIndicator(close=data['close'], window=periods, fillna=False)
    rsi_ = rsi._rsi
    return rsi_

def MovingAverageConvergenceDivergence(data = pd.DataFrame, slow=26, fast=12, signal=9, backtest: bool = False, verbose=debugLog):
    macd = MACD(close=data['close'], slow=slow, fast=fast, signal=signal, fillna=False)
    macd_ = macd._macd
    signal_ = macd._macd_signal
    diff_ = macd._macd_diff
    return macd_, signal_, diff_

def BollingerBands(data, period = 20, std_dev = 2):
    bb = BollBands(data, period, std_dev, fillna=False)
    h_band = bb._hband
    l_band = bb._lband
    m_band = bb._mavg
    return h_band, l_band, m_band


def Supertrend(data, ATR=3, ATR_Mult=7.0):
    basic_upper = (data['high'] + data['low'])/2 + ATR_Mult * ATR
    basic_lower = (data['high'] + data['low'])/2 - ATR_Mult * ATR
    #finalbandupper = 

def AwsomeOscillator(data, period1, period2):
    a_o = AweOsc(high=data['high'],low=data['low'], window1=period1, window2=period2, fillna=False)

class IndicatorType(enum.Enum):
    ERROR = -1
    NULL = 0
    CUSTOM = enum.auto()
    VALUE_LINE = enum.auto()
    VALUE_POINT = enum.auto()
    CURRENCY_LINE = enum.auto()
    CURRENCY_POINT = enum.auto()
    PERCENTAGE_LINE = enum.auto()
    HISTOGRAM_BAR = enum.auto()
    BANDS = enum.auto()
    FILL = enum.auto()
    TRADE_SIGNAL = enum.auto()
ind_t = IndicatorType()

all_indicators = {
    ''' Indicators dictionary -
        "name": (<method call>, indicatortype '''
    'SMA': (SimpleMovingAverage, ind_t.CURRENCY_LINE),
    'EMA': (ExponentialMovingAverage, ind_t.CURRENCY_LINE),
    'TEMA': (TripleExponentialMovingAverage, ind_t.CURRENCY_LINE),
    'RSI': (RelativeStrengthIndex, ind_t.PERCENTAGE_LINE),
    'MACD': (MovingAverageConvergenceDivergence[0], [ind_t.HISTOGRAM_BAR, ]),
    'BBANDS': (BollingerBands, ind_t.BANDS),
    'STREND': (Supertrend, [ind_t.TRADE_SIGNAL, ind_t.BANDS])
}
