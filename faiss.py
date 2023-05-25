import pandas as pd 
import numpy as np 
df = pd.read_csv("./csv/tmdb_5000_movies.csv")
print(df.head(8))
#构建IDS
ids = df["id"].values.astype(np.int64)
type(ids) , ids.shape

ids.dtype
ids_size = ids.shape[0]
print(ids_size)

import json 
import numpy 
datas = [] 

for x in df["genres"]:
    datas.append(json.loads(x))
    print(json.loads(x))
