
#imports 
import pandas as pd
import random
import numpy as np

#importar tabla
#printeo los datos que son guardados y sus tipos
df = pd.read_csv("clientes-centro-comercial.csv")
print("\nLa cantidad de filas que tenemos es de: ",len(df))
print("\nAqui van las diferentes columnas y sus tipos de datos dentro de ellas \n")
print(df.dtypes)
#usando minimo y maximo imprimo cuales son los rangos con los qu estamos trabajando
print("\nEl rango de Edad va desde: ", df['Edad'].min(), " hasta ", df['Edad'].max())
print("El rango de Ingresos Anuales va desde: ", df['Ingresos Anuales (k$)'].min(), " hasta ", df['Ingresos Anuales (k$)'].max())
print("El rango de Puntos en compras va desde: ", df['Puntos en compras (1-100)'].min(), " hasta ", df['Puntos en compras (1-100)'].max())

#creo un dataframe de hombres
filtro_hombres = df[ (df['Genero'] == "Hombre")]
filtro_mujeres = df[ (df['Genero'] == "Mujer")]
#hago lo mismo del rango pero en hombres
print("\nEl rango de Edad (Hombres) va desde: ", filtro_hombres['Edad'].min(), " hasta ", filtro_hombres['Edad'].max())
print("El rango de Ingresos Anuales (Hombres) va desde: ", filtro_hombres['Ingresos Anuales (k$)'].min(), " hasta ", filtro_hombres['Ingresos Anuales (k$)'].max())
print("El rango de Puntos en compras (Hombres) va desde: ", filtro_hombres['Puntos en compras (1-100)'].min(), " hasta ", filtro_hombres['Puntos en compras (1-100)'].max())
#hago lo mismo del rango pero en mujeres
print("\nEl rango de Edad (Mujer) va desde: ", filtro_mujeres['Edad'].min(), " hasta ", filtro_mujeres['Edad'].max())
print("El rango de Ingresos Anuales (Mujer) va desde: ", filtro_mujeres['Ingresos Anuales (k$)'].min(), " hasta ", filtro_mujeres['Ingresos Anuales (k$)'].max())
print("El rango de Puntos en compras (Mujer) va desde: ", filtro_mujeres['Puntos en compras (1-100)'].min(), " hasta ", filtro_mujeres['Puntos en compras (1-100)'].max())

#imprimo los ingresos generales calculando el promedio
print("\nPromedio de Ingresos general: ")
sorted_df = df['Ingresos Anuales (k$)'].sort_values()
sorted_df = sorted_df.reset_index(drop=True)
p = 5
print(sorted_df[p:-p].mean())

#imprimo los ingresos de hombres calculando el promedio
print("\nPromedio de Ingresos Hombres: ")
sorted_hombres = filtro_hombres['Ingresos Anuales (k$)'].sort_values()
sorted_hombres = sorted_hombres.reset_index(drop=True)
p = 5
print(sorted_hombres[p:-p].mean())

#imprimo los ingresos de mujeres calculando el promedio
print("\nPromedio de Ingresos Mujeres: ")
sorted_mujeres = filtro_mujeres['Ingresos Anuales (k$)'].sort_values()
sorted_mujeres = sorted_mujeres.reset_index(drop=True)
p = 5
print(sorted_mujeres[p:-p].mean())


# creo dataframes con rangos de edades

print("\nPromedio de ingresos por edad:" )
filtro_jovenes = df[ (df['Edad'] <= 30)]
filtro_medio = df[ (df['Edad'] > 30) & (df['Edad'] <= 60)]
filtro_viejos = df[ (df['Edad'] > 60)]


#imprimo los ingresos de jovenes calculando el promedio
print("\nPromedio de Ingresos Jovenes (<= 30): ")
sorted_jovenes = filtro_jovenes['Ingresos Anuales (k$)'].sort_values()
sorted_jovenes = sorted_jovenes.reset_index(drop=True)
p = 5
print(sorted_jovenes[p:-p].mean())

#imprimo los ingresos de middle aged calculando el promedio
print("\nPromedio de Ingresos Medios (>30 y <= 50): ")
sorted_medio = filtro_medio['Ingresos Anuales (k$)'].sort_values()
sorted_medio = sorted_medio.reset_index(drop=True)
p = 5
print(sorted_medio[p:-p].mean())

#imprimo los ingresos de viejos calculando el promedio
print("\nPromedio de Ingresos Viejos (>50): ")
sorted_viejos = filtro_viejos['Ingresos Anuales (k$)'].sort_values()
sorted_viejos = sorted_viejos.reset_index(drop=True)
p = 5
print(sorted_viejos[p:-p].mean())


#imprimo los ingresos de hombres calculando el promedio
print("\nPromedio de Puntos Hombres: ")
sorted_hombres = filtro_hombres['Puntos en compras (1-100)'].sort_values()
sorted_hombres = sorted_hombres.reset_index(drop=True)
p = 5
print(sorted_hombres[p:-p].mean())

#imprimo los ingresos de mujeres calculando el promedio
print("\nPromedio de Puntos Mujeres: ")
sorted_mujeres = filtro_mujeres['Puntos en compras (1-100)'].sort_values()
sorted_mujeres = sorted_mujeres.reset_index(drop=True)
p = 5
print(sorted_mujeres[p:-p].mean())

moda = df['Genero'].mode()
print(moda, "Hay mas mujeres")

print("\nMean de todo junto")
print(df.groupby(['Genero']).mean())

print("\nModa de todo junto")
moda = df['Genero'].mode()
print(moda, "\nHay mas mujeres")

print("\nMedian de todo junto")
print(df.groupby(['Genero']).median())


sdm = filtro_mujeres['Ingresos Anuales (k$)'].std()
sdh = filtro_hombres['Ingresos Anuales (k$)'].std()

print("\nDesviaciones estandar de ingresos por genero: ")
print("Mujer: ", sdm)
print("Hombre: ",sdh)


#imprimo los puntos calculando el promedio
print("\nPromedio de Puntos en compras (1-100) Jovenes (<= 30): ")
sorted_jovenes = filtro_jovenes['Puntos en compras (1-100)'].sort_values()
sorted_jovenes = sorted_jovenes.reset_index(drop=True)
p = 5
print(sorted_jovenes[p:-p].mean())

#imprimo los puntos de middle aged calculando el promedio
print("\nPromedio de Puntos en compras (1-100) (>30 y <= 60): ")
sorted_medio = filtro_medio['Puntos en compras (1-100)'].sort_values()
sorted_medio = sorted_medio.reset_index(drop=True)
p = 5
print(sorted_medio[p:-p].mean())

#imprimo los puntos de viejos calculando el promedio
print("\nPromedio de Puntos en compras (1-100) Viejos (>60): ")
sorted_viejos = filtro_viejos['Puntos en compras (1-100)'].sort_values()
sorted_viejos = sorted_viejos.reset_index(drop=True)
p = 5
print(sorted_viejos[p:-p].mean())