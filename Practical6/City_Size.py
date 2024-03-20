uk_cities=[0.56,0.62,0.04,9.7]
cn_cities=[0.58,8.4,29.9,22.2]
#Define lists to store population data of UK and Chinese cities
uk_cities.sort()
cn_cities.sort()
#Sort the population data in ascending order
print(uk_cities)
print(cn_cities)
#Print the sorted population data
import numpy as np
import matplotlib.pyplot as plt
#Import NumPy and Matplotlib libraries
uk_name=["Stirling","Edinburgh","Glasgow","London"]
cn_name=["Haining","Hangzhou","Beijing","Shanghai"]
#Define lists of city names for UK and China
plt.figure()#Create a figure for the UK city bar plot
plt.bar(uk_name,uk_cities,color="#00BFFF")
#Plot a bar chart for UK cities with population data and city names, using a specific color
plt.rcParams['font.family'] = ['Times New Roman']
plt.rcParams['font.size'] = 24
#Set font family and size
plt.ylabel("Population/million")
plt.title("city size (UK)")
#Add ylabel and title for the UK city plot
plt.figure()
#Create a new figure for the China city bar plot
plt.bar(cn_name,cn_cities,color="#FF69B4")
#Plot a bar chart for China cities with population data and city names, using a specific color
plt.rcParams['font.family'] = ['Times New Roman']
plt.rcParams['font.size'] = 24
#Set font family and size
plt.ylabel("Population/million")
plt.title("city size (China)")
#Add ylabel and title for the China city plot
plt.show()
plt.clf()
#Display the plots
#Clear the current figure













