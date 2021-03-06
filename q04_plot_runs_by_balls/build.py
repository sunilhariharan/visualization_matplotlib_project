# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)

def plot_runs_by_balls():
    ipl=ipl_df.groupby(['match_code','batsman']).agg({'runs':'sum','delivery':'count'})
    plt.scatter(ipl.loc[:,'delivery'],ipl.loc[:,'runs'])
    plt.show()
ipl=ipl_df.groupby(['match_code','batsman']).agg({'runs':'sum','delivery':'count'})
ipl.loc[:,'runs']


