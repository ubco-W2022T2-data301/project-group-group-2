#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")


# In[3]:

def load_Date_Value_Housing():
    df_index = (pd.read_csv("../../data/raw/Montly Data/Montly-index.csv")
               .drop(["UOM_ID","SCALAR_ID", "COORDINATE","SYMBOL","TERMINATED","DECIMALS"], axis =1)
               .groupby(["REF_DATE","VALUE"]).agg('mean','count')
               .dropna())
        return df_index


# In[4]:

def load_Date_Value_Housing_2007_2009():
    df_index = (pd.read_csv("../../data/raw/Montly Data/Montly-index.csv")
               .drop(["UOM_ID","SCALAR_ID", "COORDINATE","SYMBOL","TERMINATED","DECIMALS"], axis =1)
               .groupby(["REF_DATE","VALUE"]).agg('mean','count')
               .dropna()
               .reset_index()
               .assign(REF_DATE = lambda x: pd.to_datetime(x['REF_DATE']))
               .loc[(df_index['REF_DATE'] >= '2007-01-01') & (df_index['REF_DATE'] < '2010-01-01')]
               )
    return df_index

def load_Date_Value_Housing_2019_2022():
    df_index = (pd.read_csv("../../data/raw/Montly Data/Montly-index.csv")
               .drop(["UOM_ID","SCALAR_ID", "COORDINATE","SYMBOL","TERMINATED","DECIMALS"], axis =1)
               .groupby(["REF_DATE","VALUE"]).agg('mean','count')
               .dropna()
               .reset_index()
               .assign(REF_DATE = lambda x: pd.to_datetime(x['REF_DATE']))
               .loc[(df_index['REF_DATE'] >= '2019-01-01') & (df_index['REF_DATE'] < '2022-01-01')]
               )
    return df_index

# In[ ]:




