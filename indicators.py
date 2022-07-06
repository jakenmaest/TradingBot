# Indicators are stored in a dictionary with the name as key, and 
# the function as the value. This can be called from a strategy either
# with or without parameters.

# TODO - move to constants file and enumerate
UPDATE_OPEN = 0
UPDATE_CLOSE = 1
UPDATE_SEC = 2
UPDATE_MIN = 3
UPDATE_HOUR = 4
UPDATE_DAY = 5

import pandas as pd
import ta
## SETUP ##

#import ccxt
from Values import BYBIT_API_KEY, BYBIT_API_SECRET, OHLCV_DIR
#import Utilities as utils
import pandas as pd
pd.set_option('display.max_rows', None)
import warnings
warnings.simplefilter(action='ignore')

# Switch Logging off and on
debugLog = True
#bybit = ccxt.bybit({'apiKey': BYBIT_API_KEY, 'secret': BYBIT_API_SECRET})
data_dir = OHLCV_DIR

## Test Data ##
base_cur = "USDT"
exch_cur = "DOGE"
symbol = '_'.join([exch_cur, base_cur])
timeframe = "5m"
maxCandles = 500
runUpCandles = 0
jsonfile = f"{data_dir}{symbol}-{timeframe}.json"
print(jsonfile)
df = pd.read_json(jsonfile)
df.head()
#df = df[-500:-2]
#df.columns = ['timestamp','open','high','low','close','volume']
#df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
#df['trade'] = 'no_trade'
#trades = pd.DataFrame(columns=['time', 'leverage', 'fees', 'side', 'stake', 'entry_price', 'exit_price', 'percent_difference', 'PNL', 'entry_reason', 'exit_reason', 'entry_balance', 'exit_balance', 'status'])
#superTrend(df, multiplier=5, period=9)
#df_backup = df.copy()
##############
# Indicators #
##############

def SimpleMovingAverage(periods: int = 10, data = pd.DataFrame, backtest: bool = False, verbose=debugLog):
    ''' Get simple moving average of pair given periods \n
            If backtest == True, returns a pandas Series, else returns a float  '''
    if not backtest:
        per = 0-periods
        sum = data[per:].sum()
        if verbose: print(f"sum = {sum}")
        return float(sum/periods)
    # Do backtesting

indicators = {
    ''' Indicators dictionary "name": <method call> '''
    'SMA': SimpleMovingAverage
}

