Act = {"Sleeping":8,"Classes":6,"Studying":3.5,"TV":2,"Music":1}
Sl=Act["Sleeping"]
Cl=Act["Classes"]
St=Act["Studying"]
tv=Act["TV"]
mu=Act["Music"]
ot=24-Sl-Cl-St-tv-mu
Act["other"]=ot
print(Act)
import matplotlib.pyplot as plt
Activity_labels=list(Act.keys())
time=[Sl,Cl,St,tv,mu,ot]
plt.figure()
plt.pie(time,labels=Activity_labels)
plt.title("Average time")
plt.show()
plt.clf()

