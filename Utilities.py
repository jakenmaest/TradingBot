##
## Tradebot header data
##

#import OHLCV
## SETUP ##

from enum import Enum
import ccxt
from Values import BYBIT_API_KEY, BYBIT_API_SECRET, OHLCV_DIR
import pandas as pd
import warnings
from pybit import usdt_perpetual

pybit_auth = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET
)

# Switch Logging off and on
debugLog = True

warnings.simplefilter(action='ignore')
pd.set_option('display.max_rows', None)

bybit = ccxt.bybit({'apiKey': BYBIT_API_KEY, 'secret': BYBIT_API_SECRET})
data_dir = OHLCV_DIR

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

     ## FUNCTIONS ##

 # Get Balance fetch_balance dict_keys(['info', 'ADA', 'BIT', 'BTC', 'DOT', 'EOS',
#                                      'ETH', 'LTC', 'LUNA', 'MANA', 'SOL', 'USDT',
#                                      'XRP', 'free', 'used', 'total'])
def GetTotalBalance(verbose=debugLog) -> dict:
    full_balances = bybit.fetch_balance()
    totals = full_balances['total']
    balance = {}
    for t in totals:
        if totals[t] > 0:
            balance[str(t)] = totals[t]
    return balance
#print(GetTotalBalance())
def GetFreeBalance(verbose=debugLog) -> dict:
    full_balances = bybit.fetch_balance()
    totals = full_balances['free']
    balance = {}
    for t in totals:
        if totals[t] > 0:
            balance[str(t)] = totals[t]
    return balance
#print(GetFreeBalance())
def GetUsedBalance(verbose=debugLog) -> dict:
    full_balances = bybit.fetch_balance()
    totals = full_balances['used']
    balance = {}
    for t in totals:
        if totals[t] > 0:
            balance[str(t)] = totals[t]
    return balance
#print(GetUsedBalance())

 # Get all symbol ids, or all of a given quote currency
def GetSymbols(quote_currency="", verbose=debugLog) -> list:
    marketsFull = bybit.fetch_markets()
    symbols = []
    count = 0
    if quote_currency == "":
        for m in marketsFull:
            symbols.append(m['id'])
    else:
        for m in marketsFull:
            if m['quote'] == quote_currency:
                symbols.append(m['id'])
    if verbose: print(f"count: {len(symbols)}")
    return symbols
#print(GetSymbols('USDT'))

def GetTop24hVol(number: int=0, stripped: bool=True, verbose: bool=debugLog) -> tuple:
    if number > 99:
        if verbose: print("Please pick a smaller number")
        return ()
    tickers = bybit.fetch_tickers()
    all_tickers_sym = tickers.keys()
    vols = {}
    for key in all_tickers_sym:
        tick = tickers[key]
        if  tick['info']['symbol'][-4:] == 'USDT':
            vol = float(tick['quoteVolume']) * tick['last']
            vols[vol] = key
    sorted_vol = sorted(vols.items())
    sorted_vol = list(reversed(sorted_vol))
    if number > 0: sorted_vol = sorted_vol[:number]
    if stripped:
        stripped_list = []
        for res in sorted_vol:
            # BTC/USDT:USDT -> BTCUSDT
            stripped_list.append("".join(res[1].split(':')[0].split('/')))
        sorted_vol = stripped_list
    return tuple(sorted_vol)
#print(GetTop24hVol(20, True, True))

 # Create a Simple Buy/Sell Market Order
# amount - size of position in base currency
def CreateSimpleMarketOrder(sym: str = 'ADAUSDT', side: str = 'buy', amount: float = 1.0, verbose=debugLog) -> dict:
    return bybit.create_market_order(sym, side, amount, 0)
#print(CreateSimpleMarketOrder('XRPUSDT'))

 # Create a Simple Buy/Sell Limit Order
def CreateSimpleLimitOrder(sym: str = 'ADAUSDT', side: str = 'buy', amount: float = 1.0, price: float = 0.48, verbose=debugLog) -> dict:
    return bybit.create_limit_order(sym, side, amount, price)
#print(CreateSimpleLimitOrder('XRPUSDT', amount=10))

# TODO #
def CreatSimpleConditionalOrder():
    return bybit.create_contract_order()

 # Get open positions
def GetOpenPositions() -> dict:
    my_positions = pybit_auth.my_position()['result']
    positions = {}
    for p in my_positions:
        if p['data']['size'] > 0: positions[p['data']['symbol']] = p['data']
    return positions
#print(GetOpenPositions())

 # Get All active limit orders
def GetActiveOrders(symbol_list: list = []) -> list:
    limits = []
    # default list
    if symbol_list == []: symbol_list =  list(GetTop24hVol(20, True, False))
    for sym in symbol_list:
        my_order = pybit_auth.get_active_order(symbol=sym)['result']['data']
        #print(my_order)
        if my_order != None:
            for ord in my_order:
                if ord['order_status'] != 'Filled' and ord['order_status'] != 'Cancelled': limits.append(ord)
    return limits
#print(GetActiveOrders())

 # Get All active conditional orders
def GetConditionalOrders(symbol_list: list = []) -> list:
    conditionals = []
    # default list
    if symbol_list == []: symbol_list = list(GetTop24hVol(20, True, False))
    for sym in symbol_list:
        my_order = pybit_auth.get_conditional_order(symbol=sym)['result']['data']
        #print(my_order)
        if my_order != None:
            for ord in my_order:
                if ord['order_status'] != 'Filled' and ord['order_status'] != 'Deactivated': conditionals.append(ord)
    return conditionals
#print(GetConditionalOrders())

def GetCandles(symbol: str = "DOGEUSDT", timeframe='5min', start: float = 0.0, end: float = 0.0):
   '''Get Candles'''
   return
