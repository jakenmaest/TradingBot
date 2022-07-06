# Main Strategy Class

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
class Strategy:
    ''' Base Strategy Class '''
    def __init__(self, symbol='', strat_data={}):
        # init members
        if 'symbol' in strat_data: self.symbol = strat_data['symbol']
        if symbol != '': self.symbol = symbol # override strat_data if present
        if 'trade_size' in strat_data: self.tradeSize = strat_data['trade_size']
        else: self.tradeSize = 1
        if 'primary_indicators' in strat_data: self.indicators = strat_data['primary_indicators']
        else: self.indicators = []
    
    def Begin(self): pass
    def UpdateIndicators(self): pass
    def CheckTriggers(self, indicators=[]): pass
    def CheckExit(self, indicators=[]): pass
    def CheckEntry(self, indicators=[]): pass
    def UpdateSystem(self): pass
