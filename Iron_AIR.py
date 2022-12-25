
#%% md
#This is the IRON AIR project based in data collected from the WHOOP band.
#%% md
#IMPORT LIBRERIES
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#%% md
## READ DATA
#%%
jouarnals = pd.read_csv("/Users/adrianinfantesromero/Desktop/AIR/Work/GitHub/Iron_AIR/my_whoop_data_2022_12_14/journal_entries.csv")
physiological_cycles = pd.read_csv("/Users/adrianinfantesromero/Desktop/AIR/Work/GitHub/Iron_AIR/my_whoop_data_2022_12_14/physiological_cycles.csv")
sleeps = pd.read_csv("/Users/adrianinfantesromero/Desktop/AIR/Work/GitHub/Iron_AIR/my_whoop_data_2022_12_14/sleeps.csv")
woorkouts = pd.read_csv("/Users/adrianinfantesromero/Desktop/AIR/Work/GitHub/Iron_AIR/my_whoop_data_2022_12_14/workouts.csv")
#%%
jouarnals
#%%
physiological_cycles
#%%
woorkouts
#%%
sleeps
#%% md
#Just after reading these first csv we realize that the phisiological_cycles dataset gives us almost 99% of the same data as the sleeps dataset
#%%
jouarnals.info()
#%%
physiological_cycles.info()
#%%
woorkouts.info()
#%%
sleeps.info()
#%%
jouarnals.columns
#%%
physiological_cycles.columns
#%%
sleeps.columns
#%%
woorkouts.columns
#%% md
#NULL DATA SEARCH
#%%
jouarnals.isnull().sum()
#%%
physiological_cycles.isnull().sum()
#%%
sleeps.isnull().sum()
#%%
woorkouts.isnull().sum()
#%% md
## EDA Analysing Data [PHYSIOLOGICAL CYCLES]
#%%
physiological_cycles['month'] = pd.DatetimeIndex(physiological_cycles['Cycle start time']).month
physiological_cycles['day'] = pd.DatetimeIndex(physiological_cycles['Cycle start time']).day
#%%
physiological_cycles
#%%
physiological_cycles['month'].value_counts()
#%%
physiological_cycles['Blood oxygen %'].value_counts()
#%%
physiological_cycles['Skin temp (celsius)'].value_counts()
#%%
physiological_cycles['Recovery score %'].value_counts()
#%%
physiological_cycles.groupby('month')['Recovery score %'].mean()
#%%
sns.lineplot(x='month', y='Recovery score %', data=physiological_cycles, ci=95)
#%%
sns.lineplot(x='month', y='Heart rate variability (ms)', data=physiological_cycles, ci=95)
#%%
sns.lineplot(x='month', y='Day Strain', data=physiological_cycles, ci=95)
#%%
sns.lineplot(x='month', y='Energy burned (cal)', data=physiological_cycles, ci=95)
#%%
sns.lineplot(x='month', y='Sleep performance %', data=physiological_cycles, ci=95)
#%%
physiological_cycles.info()
#%%
sns.lineplot(x='month', y='Deep (SWS) duration (min)', data=physiological_cycles, ci=95)
#%%
