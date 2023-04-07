import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_and_process(url):
    df = (pd.read_csv(url)
          .rename(columns={'GEO':'PLACE', 'REF_DATE':'DATE', 'New housing price indexes': 'PLOT'})
          .drop(columns=["DGUID", "UOM", "UOM_ID", "SCALAR_ID","SCALAR_FACTOR", "COORDINATE", 'TERMINATED', 'SYMBOL', 'STATUS', 'DECIMALS', 'VECTOR'])
         )
    df = df[df['PLOT'] == "Total (house and land)"]
    df['DATE'] = pd.to_datetime(df['DATE'])
    df['MONTH'] = df['DATE'].dt.month
    return df

def value_mean_progression():
     df = (pd.read_csv(url)
          .rename(columns={'GEO':'PLACE', 'REF_DATE':'DATE', 'New housing price indexes': 'PLOT'})
          .drop(columns=["DGUID", "UOM", "UOM_ID", "SCALAR_ID","SCALAR_FACTOR", "COORDINATE", 'TERMINATED', 'SYMBOL', 'STATUS', 'DECIMALS', 'VECTOR'])
         )
    df = df[df['PLOT'] == "Total (house and land)"]
    df['DATE'] = pd.to_datetime(df['DATE'])
    df['MONTH'] = df['DATE'].dt.month
    df.groupby(["MONTH","VALUE"]).agg('mean','count')
    return df

def value_max_progression():
     df = (pd.read_csv(url)
          .rename(columns={'GEO':'PLACE', 'REF_DATE':'DATE', 'New housing price indexes': 'PLOT'})
          .drop(columns=["DGUID", "UOM", "UOM_ID", "SCALAR_ID","SCALAR_FACTOR", "COORDINATE", 'TERMINATED', 'SYMBOL', 'STATUS', 'DECIMALS', 'VECTOR'])
         )
    df = df[df['PLOT'] == "Total (house and land)"]
    df['DATE'] = pd.to_datetime(df['DATE'])
    df['MONTH'] = df['DATE'].dt.month
    df.groupby('MONTH')['VALUE'].max().reset_index()
    return df



def value_max_place():
     df = (pd.read_csv(url)
          .rename(columns={'GEO':'PLACE', 'REF_DATE':'DATE', 'New housing price indexes': 'PLOT'})
          .drop(columns=["DGUID", "UOM", "UOM_ID", "SCALAR_ID","SCALAR_FACTOR", "COORDINATE", 'TERMINATED', 'SYMBOL', 'STATUS', 'DECIMALS', 'VECTOR'])
         )
    df = df[df['PLOT'] == "Total (house and land)"]
    df['DATE'] = pd.to_datetime(df['DATE'])
    df['MONTH'] = df['DATE'].dt.month
    exclude = ['Alberta', 'British Columbia', 'Canada', 'Manitoba', 'Ontario', 'Quebec', 'Saskatchewan','Atlantic Region','New Brunswick','Nova Scotia','Prairie Region']
    df['PLACE'] = df['PLACE'].apply(lambda x: x if x not in exclude else '')
    df.groupby('PLACE')['VALUE'].max().reset_index()
    return df


