
## Create a system for graphing market data by 
# a timeframe set by the main graph. This main graph
# shuld be displaying market candles, and other
# currency based values, other graphs will be
# displayed below, maybe a percentage value graph,
# and then a histogram below that. Graphs should be
#  mergable and splittable both with the main graph, 
# and other graphs. Different timeframes from the main
# should have the appropriate zoom on the x axis, in 
# respect to the main graph timeframe. combined graphs
# with different y axis units will utilize both sides of
# the graph (2 max for now).
#
#  Strategy page - RSI_MACD_Intermediate
#       Main Graph (5min, zoom:1x)
#           Candles
#           Trade Data
#           EMA_Ribbons
#       Second Graph (5mins, zoom:1x)
#           RSI
#           Stoch.
#       Third Graph (1min, zoom:5x)
#           MACD
#           MACD_Signal
#           MACD_Diff
#

graphs = []
maintimeframe = '5min'
def AddGraph(indicators=[], timeframe=maintimeframe, onChart=0): pass
