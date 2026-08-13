import matplotlib.pyplot as plt
import pandas as pd
import numpy as npy
#Pego meu df
df=pd.read_csv("timeline.csv")

#Tranformo em unidade de tempo
df.month=pd.to_datetime(df.month)

#Coloco como meu indice tranfotmando em uma série temporal.
df.set_index("month",inplace=True)

def m(args):
    print(args)
