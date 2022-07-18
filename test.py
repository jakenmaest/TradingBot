from time import mktime, time
from Utilities import GetOCHLV, TimeFormat, bybit

from time import mktime
from datetime import datetime as date_time

base_cur = "USDT"
exch_cur = "DOGE"
file_sym = ''.join([exch_cur, base_cur])

# Seconds in certain timeframe
TSTAMP_1_MIN = 60.0
TSTAMP_5_MIN = 300.0
TSTAMP_10_MIN = 600.0
TSTAMP_15_MIN = 900.0
TSTAMP_20_MIN = 1200.0
TSTAMP_30_MIN = 1800.0
TSTAMP_45_MIN = 2700.0
TSTAMP_1_HOUR = 3600.0
TSTAMP_1_DAY = 86400.0
TSTAMP_1_WEEK = 604800

# No time specified
sTime = date_time(2021, 1, 1)
eTime = date_time(2021, 12, 31)

sTstamp = mktime(sTime.timetuple()) # start of start day
eTstamp = mktime(eTime.timetuple()) + TSTAMP_1_DAY # end of end day

if __name__ == "__main__":
    #print(f"start {date_time.fromtimestamp(sTstamp)}:{sTstamp}")
    #print(f"finish {date_time.fromtimestamp(eTstamp)}:{eTstamp}")
    t1 = time()
    df1 = GetOCHLV(symbol=file_sym, timeframe='5m', start=sTstamp, end=eTstamp)
    t2 = time()
    print(f"time: {t2-t1:.2f}")
    print(df1.describe())

