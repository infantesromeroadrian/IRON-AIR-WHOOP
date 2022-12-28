
#IRON AIR PROJECT
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
sns.lineplot(x='Day Strain', y='Recovery score %', data=physiological_cycles, ci=95)
#%% md
#Esta correlacion indica que cuando el recovery score es mas alto el day strain es mas alto. Aunque el lineplot no es el mejor para este tipo de datos porque no se puede ver la distribución
#%%
sns.scatterplot(x='Day Strain', y='Recovery score %', data=physiological_cycles)
#%% md
#El scatterplot nos muestra que hay una relación lineal entre estas dos variables. y esta dice que cuanto mayor es el Day Strain, mayor es el Recovery score.
#%%
sns.jointplot(x='Day Strain', y='Recovery score %', data=physiological_cycles, kind='hex')
#%% md
#El jointplot nos muestra la distribución de los datos y la relación entre las dos variables.
#En este caso, la distribución de los datos es normal y la relación es lineal.
#Esto quiere decir que cuanto mayor es el Day Strain, mayor es el Recovery score.
#Dsitribucion de datos normal quiere decir que la media y la mediana son iguales.
#La ralcion lineal quiere decir que la pendiente es positiva.
#%%
sns.regplot(x='Day Strain', y='Recovery score %', data=physiological_cycles)
#%% md
#El regplot nos muestra la distribución de los datos y la relación entre las dos variables.
#En este caso, la distribución de los datos es normal y la relación es lineal.
#Esto quiere decir que cuanto mayor es el Day Strain, mayor es el Recovery score.
#Distribucion de datos normal quiere decir que la media y la mediana son iguales y la relacion lineal quiere decir que la pendiente es positiva.

#Los puntos que se encuentran en la parte superior derecha de la gráfica son los que tienen un Day Strain mayor y un Recovery score mayor.
#Los puntos que se encuentran en la parte inferior izquierda de la gráfica son los que tienen un Day Strain menor y un Recovery score menor.
#%%
sns.heatmap(physiological_cycles.corr(), annot=True)
#%% md
#En el heatmap se puede ver la correlación entre las variables. En este caso, la correlación entre el Day Strain y el Recovery score es positiva.
#Esto quiere decir que cuanto mayor es el Day Strain, mayor es el Recovery score.
#Los colores que se encuentran en la parte superior derecha de la gráfica son los que tienen una correlación positiva.
#Los colores que se encuentran en la parte inferior izquierda de la gráfica son los que tienen una correlación negativa.