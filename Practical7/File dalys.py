import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/zhaochenghang/Desktop/IBI/IBI1_2023-24/Practical7")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
#showing the fourth column (the DALYs) from every 10th row,starting from the first row, for the first 100 rows (inclusive)
#print(dalys_data.iloc[0:101:10,3])

#show DALYs for all rows corresponding to Afghanistan
my_rolls1 = dalys_data.iloc[:,0]=="Afghanistan"
#print(dalys_data.loc[my_rolls1,"DALYs"])

#compute the mean DALYs in China over time
my_rolls2=dalys_data.iloc[:,0]=="China"
cn_da=dalys_data.loc[my_rolls2,["Year","DALYs"]]
cn_da_mean=np.mean(cn_da["DALYs"])
cn_2019=cn_da.iloc[29,1]
#print("the mean DALYs in China over time is",cn_da_mean)
#cn_2019=22270.51<30677.69, the DALYs in China in 2019 below mean

#created a plot showing the DALYS over time in China
plt.figure()
plt.plot(cn_da.Year,cn_da.DALYs,"b+")
plt.xticks(cn_da.Year,rotation=-90)
plt.show()
plt.clf()

#Answer the question
my_rolls3=dalys_data.iloc[:,0]=="Japan"
jp_da=dalys_data.loc[my_rolls3,["Year","DALYs"]]
fig,axes=plt.subplots(1,1,figsize=(6,6),dpi=100,facecolor="w")
plt.plot(jp_da.Year,cn_da.DALYs,"r+")
plt.xticks(jp_da.Year,rotation=-90)
fig.suptitle("The correlation between DALYs and time in Japan")
plt.show()
plt.clf()
