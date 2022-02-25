import pandas as pd
import pyupbit

df = pd.read_excel("data.xlsx", header=0, index_col=0)
print(df)
aa = df.loc["B", "stock_name"]
bb = df.loc["C", "stock_name"]
print(aa)
print(bb)
print(type(aa))
df.loc["B", "bought_price"] = 10
print(df)
print(pyupbit.get_tickers("KRW"))