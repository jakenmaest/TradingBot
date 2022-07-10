# Main Strategy Class
import os
import pandas as pd
from indicators import Indicators
from Utilities import GetOCHLV
## Test Data
data_dir = f"../../data/bybit/" # current historical data
jsonfile = f"{data_dir}{'DOGEUSDT'}-{'5min'}.json"
if os.path.exists(jsonfile): pass
    # Check for strategy timeframe
else: print("boo")
    # Create file
    #df = pd.read_json(jsonfile)

# TODO - Move Constants to another file and convert to enums
LEVERAGE_MODE_DEFAULT = 0
LEVERAGE_MODE_CROSSED = 1
LEVERAGE_MODE_ISOLATED = 2

# Indicators inputs are stored in a tuple with the label string at index 0,
# and parameters following ** order is essential, hence tuples **
primaryInd = [('EMA',10), ('EMA',50), ('EMA',100)]
secondaryInd = [('BBands', 10, 2), ('ATR', 5), ('Fractals', 2, 5)]
tertiaryInd = [('Supertrend', 12, 5)]

class Strategy():
    ''' Base Strategy Interface '''
    def __init__(self, strat_data={}):
        self.s_data = {
            # Default data
            'id': -1,

            'name': 'SampleEMA',
            'timeframes': ['5min'],
            'symbols': ['DOGEUSDT'],
            'start_time': '02_Jul_2022',
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

    def FillIndicators(self):
        ## Fill indicators to date
        pass

    def UpdateIndicators(self):
        ## In live/fwd-testing modes, Update all indicators
        pass

    def UpdateTriggers(self, indicators=[]):
        ## In live/fwd-testing modes, Update all indicators
        pass

    def CheckExit(self, triggers):
        # Get Trigger info to check exit info
        pass

    def CheckEntry(self, triggers):
        # Get Trigger info to check entry info
        pass

    def CommitUpdate(self, triggers): pass

    def UpdateSystem(self): pass

