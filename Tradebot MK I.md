# Tradebot MK I
## A simple server for executing trading strategies
##### TODO - Modular Indicators with conditions

### Class Members
- Strategy data - start-end, timeframe, symbol list ...
- Trading data - Amount, long/short, leverage, history ...
- Prinary Indicators - SMA, TrendDir ...
- Secondary Indicators - Bollinger bands, ATR ...
- Tertiary Indicators - Supertrend ...
- Triggers

# Strategy Data
This has all of the strategy specific data.
# Trading Data
This has all trading history and current trading status within 
the strategy.

# Indicators
I will use python libraries for most of these as they are
pre optimized, but for any custom indicators, I will use
numpy based maths, which will help efficiancy in backtesting,
and with large symbol lists. There will be an update frequency
to determine how often the indicator should be updated. An SMA only
needs to be updated once per period, where as another value may
need to be checked 100 times every period.
# Triggers
Triggers are custom indicators evaluated just after tertiary list, that will trigger a trading function. 
Outputs can be stored as a single value, or as a dataframe. to be used
by the trade functions, for example, if supertrend switches to buy, 
it could trigger a long entry. If the EMA5 > EMA100, then output could
be the difference between the two to determine trade amount. Triggers
will have a status, 

---
### Live Strategy Loop (for each symbol)
##### 0 - Init (only once)
First the strategy will run the prerequisite indicator steps,for
example, if the strategy requires a 20 period simple moving average,
the strategy will take the 20 values before the starting point.
##### 0.5 - Get Current Trade Status (only once) 
##### 1 - Update Indicators (start Loop)
All indicators should be updated in order. Trigger indicators.
##### 2 - Test exit conditions on open trades

##### 3 - Test enter conditions, enter on condition

##### 4 - Custom conditions, advanced actions
##### 5 - Update database
##### 6 - Goto 1