import tushare as tu

df = tu.get_realtime_quotes('000581') #Single stock symbol
df[['code','name','price','time']]



print ('------------------')
print (df)