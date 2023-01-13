

#This is the IRON AIR project based in data collected from the WHOOP band.
#En este proyecto vamos a analizar la correlacion que tienen los parametros fisiologicos con el recovery.
#Como el strain puede afectar a la calidad del sueño y al recovery.

#Vamos a analizar la correlacion que tienen todos estos parametros fisiologicos durante el año desde el inicio de la temporada de entrenamiento y con varias pruebas fisicas en el año hasta llegar a la prueba final que sera un IRONMan
#%% md
# 2.0 - IMPORT LIBRERIES
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#%% md
# 3.0 - READ DATA
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
#%% md
# 4.0 - ANALISING DATA - JOUARNALS
#%%
jouarnals.info()
#%%
jouarnals.count()
#%%
jouarnals.isnull().sum()
#%% md
# 4.1 - ANALISING DATA - physiological_cycles
#%%
physiological_cycles.info()
#%%
physiological_cycles.count()
#%%
physiological_cycles.isnull().sum()
#%% md
# 4.2 - ANALISING DATA - WorkOuts
#%%
woorkouts.info()
#%%
woorkouts.count()
#%%
woorkouts.isnull().sum()
#%% md
#4.2 - ANALISING DATA - Sleeps
#%%
sleeps.info()
#%%
sleeps.count()
#%%
sleeps.isnull().sum()
#%% md
# 5.0 - EDA Analysing Data [PHYSIOLOGICAL CYCLES] - 1 Variable cuantitativa
#%% md
## Conversion a fechas
#%%
physiological_cycles
#%%
physiological_cycles["Cycle start time"] = pd.to_datetime(physiological_cycles["Cycle start time"])
#%%
physiological_cycles["month"] = physiological_cycles["Cycle start time"].dt.month
physiological_cycles["day"] = physiological_cycles["Cycle start time"].dt.day
physiological_cycles["year"] = physiological_cycles["Cycle start time"].dt.year
#%% md
## 5.1 - EDA Analysing Data [Recovery %]
#%%
physiological_cycles.groupby("month")["Recovery score %"].mean()
#%%
sns.lineplot(x='month', y='Recovery score %', data=physiological_cycles, ci=95)
#%% md
#En este primer analisis podemos encontrar algumos de los primeros datos:
#- Al parecer el mes 5, 6 y 3 son los que mas alto % de recovery hemos encontrado
#- El resto de meses podemos observar que tenemos un recovery entorno al 50%
#%% md
## 5.2 - Analysing Data [Resting heart rate (bpm)]
#%%
physiological_cycles.groupby("month")["Resting heart rate (bpm)"].mean()
#%%
sns.lineplot(x='month', y='Resting heart rate (bpm)', data=physiological_cycles, ci=95)
#%% md
## 5.3 - Analysing Data [Heart rate variability (ms)]
#%%
physiological_cycles.groupby("month")["Heart rate variability (ms)"].mean()
#%%
sns.lineplot(x='month', y='Heart rate variability (ms)', data=physiological_cycles, ci=95)
#%% md
## 5.4 - Analysing Data [Skin temp (celsius)]
#%%
physiological_cycles.groupby("month")["Skin temp (celsius)"].mean()
#%%
sns.lineplot(x='month', y='Skin temp (celsius)', data=physiological_cycles, ci=95)
#%% md
## 5.5 - Analysing Data [Sleep performance %]
#%%
physiological_cycles.groupby("month")["Sleep performance %"].mean()
#%%
sns.lineplot(x='month', y='Sleep performance %', data=physiological_cycles, ci=95)
#%% md
## 5.6 - Analysing Data [Respiratory rate (rpm)
#%%
physiological_cycles.groupby("month")["Respiratory rate (rpm)"].mean()
#%%
sns.lineplot(x='month', y='Respiratory rate (rpm)', data=physiological_cycles, ci=95)
#%% md
## 5.7 - Analysing Data [Sleep efficiency %]
#%%
physiological_cycles.groupby("month")["Sleep efficiency %"].mean()
#%%
sns.lineplot(x='month', y='Sleep efficiency %', data=physiological_cycles, ci=95)
#%% md
#Hasta aqui son variables que analizan:
#- Recovery
#- Respiracion
#- Pulso en reposo
#- Descanso y su puntuacion
#Todos ellos relacionados directamente con el recovery.
#%% md
## 5.8 - Analysing Data [Day strain]
#%%
physiological_cycles.groupby("month")["Day Strain"].mean()
#%%
sns.lineplot(x='month', y='Day Strain', data=physiological_cycles, ci=95)
#%% md
## 5.9 - Analysing Data [Energy burned (cal)]
#%%
physiological_cycles.groupby("month")["Energy burned (cal)"].mean()
#%%
sns.lineplot(x='month', y='Energy burned (cal)', data=physiological_cycles, ci=95)
#%% md
#Hemos analizado la evolucion de las variables que estan relacionadas con el esfuerzo:
#- Day Strain
#- Energy burned (cal)
#%% md
# 6.0 - EDA Analysing Data [PHYSIOLOGICAL CYCLES] - Correlacion de variables cuantitativas
#%% md
## Recovery - Sleep efficiency
#%%
sns.jointplot(x='Sleep efficiency %', y='Recovery score %', data=physiological_cycles, kind='hex')
#%% md
#este grafico se interpreta de la siguiente manera: la distribucion de los datos es normal y la relacion es lineal. esto quiere decir que cuanto mayor es el Sleep efficiency, mayor es el Recovery score. dsitribucion de datos normal quiere decir que la media y la mediana son iguales. la ralcion lineal quiere decir que la pendiente es positiva. los puntos que se encuentran en la parte superior derecha de la gráfica son los que tienen un Sleep efficiency mayor y un Recovery score mayor. los puntos que se encuentran en la parte inferior izquierda de la gráfica son los que tienen un Sleep efficiency menor y un Recovery score menor.
#%% md
## Recovery - Respiratory rate
#%%
sns.jointplot(x='Respiratory rate (rpm)', y='Recovery score %', data=physiological_cycles, kind='hex')
#%% md
#Este grafico se interpreta de la siguiente manera: la distribucion de los datos es normal y la relacion es lineal. esto quiere decir que cuanto mayor es el Respiratory rate, mayor es el Recovery score. dsitribucion de datos normal quiere decir que la media y la mediana son iguales. la ralcion lineal quiere decir que la pendiente es positiva. los puntos que se encuentran en la parte superior derecha de la gráfica son los que tienen un Respiratory rate mayor y un Recovery score mayor. los puntos que se encuentran en la parte inferior izquierda de la gráfica son los que tienen un Respiratory rate menor y un Recovery score menor.
#%% md
## Recovery - Skin temperature
#%%
sns.jointplot(x='Skin temp (celsius)', y='Recovery score %', data=physiological_cycles, kind='hex')
#%% md
#Este grafico indica que la relacion entre Skin temp y Recovery score es lineal. esto quiere decir que cuanto mayor es el Skin temp, mayor es el Recovery score. la ralcion lineal quiere decir que la pendiente es positiva. los
#puntos que se encuentran en la parte superior derecha de la gráfica son los que tienen un Skin temp mayor y un Recovery score mayor. los puntos que se encuentran en la parte inferior izquierda de la gráfica son los que
#tienen un Skin temp menor y un Recovery score menor.
#%% md
## Day Strain - Energy burned
#%%
sns.jointplot(x='Day Strain', y='Energy burned (cal)', data=physiological_cycles, kind='hex')
#%% md
