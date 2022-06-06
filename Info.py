import numpy as np
import pandas as pd


def get_data(file_path, prices_data=None):
    ds = pd.read_csv(file_path)
    df = ds[['Food product', 'Farm']]
    df = df.rename(columns={'Food product': 'food_name', 'Farm': 'weight'})
    if prices_data is None:
        df['prices'] = np.random.uniform(0.1, 10, df.shape[0])
    else:
        df['prices'] = prices_data
    return df
