uk_cities=[0.56,0.62,0.04,9.7]
cn_cities=[0.58,8.4,29.9,22.2]
uk_cities.sort()
cn_cities.sort()
print(uk_cities)
print(cn_cities)
import numpy as np
import matplotlib.pyplot as plt
uk_name=["Stirling","Edinburgh","Glasgow","London"]
cn_name=["Haining","Hangzhou","Beijing","Shanghai"]
plt.figure()
plt.bar(uk_name,uk_cities)
plt.ylabel("Population/million")
plt.title("city size (UK)")
plt.figure()
plt.bar(cn_name,cn_cities)
plt.ylabel("Population/million")
plt.title("city size (China)")
plt.show()
plt.clf()