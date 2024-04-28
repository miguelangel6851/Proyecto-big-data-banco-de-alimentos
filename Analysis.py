 Cargamos la librerias que vamos a usar

import numpy as np 
import pandas as pd 
import pylab as pl  
import matplotlib.pyplot as plt
import seaborn as sns


import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

lista_stopwords = set(stopwords.words('spanish')) 
lista_stopwords.update(['el','la','','','']) 
#lista_stopwords                             



data=pd.read_csv('/content/drive/MyDrive/BASE DE TRABAJO U AMERICA.xlsx - Hoja1.csv')
data.head()

data.info()

data.describe()

for columna in data.columns:
    print(f"Valores únicos en '{columna}': {data[columna].nunique()}")

for columna in data.columns:
    print(f"Primeras filas de '{columna}':")
    print(data[columna].head())

conteo_barrios = data['BARRIO'].value_counts()
print(conteo_barrios)


plt.figure(figsize=(10, 6))
conteo_barrios.plot(kind='bar')
plt.title('Distribución de Barrios')
plt.xlabel('BARRIO')
plt.ylabel('Cantidad')
plt.show()


plt.figure(figsize=(10, 8))
plt.pie(conteo_barrios, labels=conteo_barrios.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribución de Barrios')
plt.axis('equal')  # Hace que el gráfico sea un círculo perfecto
plt.show()


conteo_organizacion = data['ORGANIZACIÓN'].value_counts()
print(conteo_organizacion)


plt.figure(figsize=(10, 6))
conteo_organizacion.plot(kind='bar')
plt.title('Distribución de organizacion')
plt.xlabel('ORGANIZACIÓN')
plt.ylabel('Cantidad')
plt.show()


plt.figure(figsize=(10, 8))
plt.pie(conteo_organizacion, labels=conteo_organizacion.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribución de organizacion')
plt.axis('equal')  # Hace que el gráfico sea un círculo perfecto
plt.show()


conteo_grupopoblacional = data['GRUPO POBLACIONAL'].value_counts()
print(conteo_grupopoblacional)


plt.figure(figsize=(10, 6))
conteo_grupopoblacional.plot(kind='bar')
plt.title('Distribución de GRUPO POBLACIONAL')
plt.xlabel('GRUPO POBLACIONAL')
plt.ylabel('Cantidad')
plt.show()


plt.figure(figsize=(10, 8))
plt.pie(conteo_grupopoblacional, labels=conteo_grupopoblacional.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribución de grupo poblacional')
plt.axis('equal')  # Hace que el gráfico sea un círculo perfecto
plt.show()


conteo_REDTERRITORIAL = data['RED TERRITORIAL'].value_counts()
print(conteo_REDTERRITORIAL)


plt.figure(figsize=(10, 6))
conteo_REDTERRITORIAL.plot(kind='bar')
plt.title('Distribución de RED TERRITORIAL')
plt.xlabel('RED TERRITORIAL')
plt.ylabel('Cantidad')
plt.show()

conteo_LOCALIDAD = data['LOCALIDAD'].value_counts()
print(conteo_LOCALIDAD)


plt.figure(figsize=(10, 6))
conteo_barrios.plot(kind='bar')
plt.title('Distribución de LOCALIDAD')
plt.xlabel('LOCALIDAD')
plt.ylabel('Cantidad')
plt.show()


conteo_LOCALIDAD = data['DIA DE PEDIDO'].value_counts()
print(conteo_LOCALIDAD)


plt.figure(figsize=(10, 6))
conteo_barrios.plot(kind='bar')
plt.title('Distribución de DIA DE PEDIDO')
plt.xlabel('DIA DE PEDIDO')
plt.ylabel('Cantidad')
plt.show()


conteo_FRECUENCIA = data['FRECUENCIA'].value_counts()
print(conteo_FRECUENCIA)


plt.figure(figsize=(10, 6))
conteo_barrios.plot(kind='bar')
plt.title('Distribución de FRECUENCIA')
plt.xlabel('FRECUENCIA')
plt.ylabel('Cantidad')
plt.show()


conteo_SEMANA = data['SEMANA'].value_counts()
print(conteo_SEMANA)



plt.figure(figsize=(10, 6))
conteo_barrios.plot(kind='bar')
plt.title('Distribución de SEMANA')
plt.xlabel('SEMANA')
plt.ylabel('Cantidad')
plt.show()



plt.figure(figsize=(10, 6))
plt.scatter(data['ORGANIZACIÓN'], data['GRUPO POBLACIONAL'])
plt.title('Relación entre ORGANIZACIÓN y GRUPO POBLACIONAL')
plt.xlabel('ORGANIZACIÓN')
plt.ylabel('GRUPO POBLACIONAL')
plt.show()



plt.figure(figsize=(10, 6))
sns.boxplot(x='BARRIO', y='GRUPO POBLACIONAL', data=data)
plt.title('Distribución de Grupos Poblacionales por Barrio')
plt.xticks(rotation=45)
plt.show()


conteo_LOCALIDAD = data['FRECUENCIA'].value_counts()
print(conteo_FRECUENCIA)


plt.figure(figsize=(10, 8))
plt.pie(conteo_FRECUENCIA, labels=conteo_FRECUENCIA.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribución de FRECUENCIA')
plt.axis('equal')  # Hace que el gráfico sea un círculo perfecto
plt.show()


plt.figure(figsize=(10, 8))
plt.pie(conteo_SEMANA, labels=conteo_SEMANA.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribución de SEMANA')
plt.axis('equal')  # Hace que el gráfico sea un círculo perfecto
plt.show()
