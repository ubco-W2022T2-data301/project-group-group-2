import seaborn as sns
import numpy as np
import pandas as pd
def load_and_process(url):
    df = (pd.read_csv(url)
    .dropna(subset="VALUE")
      .rename(columns={'GEO':'LOCATION', 'REF_DATE':'DATE', 'New housing price indexes': 'House/land'})
    .drop(columns=["DGUID", "UOM", "UOM_ID", "SCALAR_ID","SCALAR_FACTOR", "COORDINATE", 'TERMINATED', 'SYMBOL', 'STATUS', 'DECIMALS', 'VECTOR'])
     .loc[lambda x: x['House/land'].str.contains('House only')]
      .drop(columns=['House/land'])
      .assign(St_JOHNS = lambda x: x.VALUE.where(x.LOCATION.str.contains("St. John's")), 
              QUEBEC = lambda x: x.VALUE.where(x.LOCATION.str.contains("Quebec")),
              OTTAWA = lambda x: x.VALUE.where(x.LOCATION.str.contains("Ottawa")),
              VICTORIA = lambda x: x.VALUE.where(x.LOCATION.str.contains("Victoria")),
              REGINA = lambda x: x.VALUE.where(x.LOCATION.str.contains("Regina")),
              EDMONTON = lambda x: x.VALUE.where(x.LOCATION.str.contains("Edmonton")),
              HALIFAX = lambda x: x.VALUE.where(x.LOCATION.str.contains("Halifax")),
              WINNIPEG = lambda x: x.VALUE.where(x.LOCATION.str.contains("Winnipeg")),
             )
      .drop(columns='VALUE')
      .groupby('DATE')[['St_JOHNS', 'QUEBEC', 'OTTAWA', 'VICTORIA', 'REGINA', 'EDMONTON', 'HALIFAX','WINNIPEG']].first().reset_index()
     )
    return df