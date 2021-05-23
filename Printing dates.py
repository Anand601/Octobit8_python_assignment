import numpy as np
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
print("Yestraday date was: ",yesterday)

today     = np.datetime64('today', 'D')
print("Today date is: ",today)

tomorrow  = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("Tomorrow date will be: ",tomorrow)

