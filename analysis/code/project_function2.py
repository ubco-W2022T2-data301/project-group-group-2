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