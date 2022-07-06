# Main Strategy Class
import abc

# TODO - Move Constants to another file and convert to enums
LEVERAGE_MODE_DEFAULT = 0
LEVERAGE_MODE_CROSSED = 1
LEVERAGE_MODE_ISOLATED = 2
IndicatorList = []

# Indicators inputs are stored in a tuple with the label string at index 0,
# and parameters following ** order is essential, hence tuples **
primaryInd = [('EMA',10), ('EMA',50), ('EMA',100)]
secondaryInd = [('BBands', 10, 2), ('ATR', 5), ('Fractals', 2, 5)]
tertiaryInd = [('Supertrend', 12, 5)]

strategy_data = {
    'id': 1,
    'name': 'SimpleRSI',
    'symbol': 'DOGEUSDT',
    'trade_size': 1.0,
    'leverage': 1,
    'lev_mode': LEVERAGE_MODE_CROSSED,
    'primary_indicators': primaryInd,
    #'secondary_indicators': [],
    #'tertiary_indicators': tertiaryInd,
}

# Triggers have three
class IStrategy(abc.ABC):
    ''' Base Strategy Interface '''
    def __init__(self, symbol='', strat_data={}): pass
    
    @abc.abstractmethod
    def Begin(self): pass
    @abc.abstractmethod
    def UpdateIndicators(self): pass
    @abc.abstractmethod
    def CheckTriggers(self, indicators=[]): pass
    @abc.abstractmethod
    def CheckExit(self, indicators): pass
    @abc.abstractmethod
    def CheckEntry(self, indicators): pass
    @abc.abstractmethod
    def UpdateSystem(self): pass

