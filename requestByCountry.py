import pandas as pd
from functools import reduce

data = pd.read_csv("datasets/website-access.data",header=None,sep=" ")
ok=data.groupby(data[0]).size()
print(reduce(lambda acc, val: acc + val, ok))

print(ok)