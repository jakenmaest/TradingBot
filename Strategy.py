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

# Load List of strategies from a file

# Triggers have three
class Strategy(abc.ABC):
    ''' Base Strategy Interface '''
    def __init__(self, strat_data={}):
        self.s_data = {
            'id': -1,
            'name': 'SampleEMA',
            'timeframes': ['5min'],
            'symbols': ['DOGEUSDT'],
            'start_time': '02_Jul_2022_00:00.00Z',
            'end_time' : '09_Jul_2022_00:00.00Z',
            'trade_size': 1.0,
            'leverage': 1,
            'lev_mode': LEVERAGE_MODE_CROSSED,
            'primary_indicators': [('EMA',10), ('EMA',50), ('EMA',100)],
            'triggers': {
                """ Triggers - 'name':(Operand1, Operator, Operand2, Result)
                    Results are in '&' seperated list format, operands can use
                    other logic such as 'EMA50|EMA100' as EMA50 or EMA500 """
                'uptrend': ('EMA10','>', 'EMA50&EMA100', 't_uptrend=True&t_downtrend=False'),
                'downtrend':('EMA10','>', 'EMA50&EMA100', 't_uptrend=False&t_downtrend=True')
            }
        }

    #@abc.abstractmethod
    def Begin(self):
        ## Retrieve all OCHLV data for relevant timeframes
        
        ## Add all Indicators and triggers to date    
        pass

    def FillOCHLV(self):
        ## Parse parameters
        ## Check for previous data Candle data
        pass
    @abc.abstractmethod
    def FillIndicators(self):
        ## Fill indicators to date
        pass

    #@abc.abstractmethod
    def UpdateIndicators(self):
        ## In live/fwd-testing modes, Update all indicators
        pass

    #@abc.abstractmethod
    def UpdateTriggers(self, indicators=[]):
        ## In live/fwd-testing modes, Update all indicators
        pass

    #@abc.abstractmethod
    def CheckExit(self, triggers):
        # Get Trigger info to check exit info
        pass

    #@abc.abstractmethod
    def CheckEntry(self, triggers):
        # Get Trigger info to check entry info
        pass

    #@abc.abstractmethod
    def CommitUpdate(self, triggers): pass

    #@abc.abstractmethod
    def UpdateSystem(self): pass
