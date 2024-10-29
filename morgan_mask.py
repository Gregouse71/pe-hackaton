import numpy as numpy
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display


exoplanetes=pd.read_csv('exoplanetes.csv',comment='#')



exoplanetes_sample=exoplanetes.iloc[:100]

Earth_like={}
Earth_like['pl_rade']=(0.5,2)
Earth_like['pl_masse']=(0.5,2)
Earth_like['pl_orbeccen']=(0,0.2)

Earth_like['st_teff']=(4500,7000)
Earth_like['st_mass']=(0.1,10)




def dict_to_mask(df,dict):
    mask=df['disc_year'] > 0
    keys=['pl_name','sy_dist']
    for key in dict:
        keys.append(key)
        if type(dict[key]) == tuple:
            mask_key = (df[key] >= dict[key][0]) & (df[key] <= dict[key][1])
       
        else:
            mask_key = df[key] == dict[key]
        
        mask = mask & mask_key

    return df[mask][keys]

df=dict_to_mask(exoplanetes,Earth_like)
print(df)

#exoplanetes_filt_pl_orbper.groupby('pl_orbper').count()['pl_name'].plot(style='.')
