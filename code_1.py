import numpy as numpy
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display


exoplanetes=pd.read_csv('exoplanetes.csv',comment='#')

exoplanetes_sample=exoplanetes.iloc[:100]

period={}
period['pl_orbper' ]=(150,1000)
perio['pl_rade']=(0.6,2)

def dict_to_mask(df,dict):
    mask=df['disc_year'] > 0
    for key in dict:
        if type(dict[key]) == tuple:
            mask_key = (df[key] > dict[key][0]) & (df[key] < dict[key][1])

        
        else:
            mask_key = df[key] == dict[key]
        
        mask = mask & mask_key

    return df[mask]

print(dict_to_mask(exoplanetes,period))

#exoplanetes_filt_pl_orbper.groupby('pl_orbper').count()['pl_name'].plot(style='.')
