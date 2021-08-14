import pandas as pd
import seaborn as sns
import numpy as np
import os
import matplotlib.pyplot as plt
import statistics as stat
from scripts import project_functions


def load_and_process(path):
    df1 = (
            pd.read_csv(path)
            .rename(columns={"LifeExp":"LifeExpectancy"})
            .dropna()
            .sort_values("Country", ascending=True)
    )
    df2 = (
            df1
            .assign(color_filter=lambda x: np.where((x.Year > 1800) & (x.LifeExpectancy > 0), 1, 0))
    )
    
    return df2
