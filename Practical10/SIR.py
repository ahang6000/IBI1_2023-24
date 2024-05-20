import numpy as np 
import matplotlib . pyplot as plt 

#define variables
N=10000
S=[9999]
I=[1]
R=[0]
t=[0] #time
beta=0.3
gamma=0.05

#Using for loops
for i in range(1,1000):
    t.append(i)
    #find the recover people,I_R means I=>R
    lis_I_R=np.random.choice(range(2),I[i-1],p=[gamma,1-gamma])
    I_R=np.sum(lis_I_R==0)
    #calculate the possibility of S=>I,"P(infect)"
    proportion=I[i-1]/N
    Pinfect=proportion*beta
    #caluculate the increased infection
    lis_S_I=np.random.choice(range(2),S[i-1],p=[1-Pinfect,Pinfect])
    S_I=np.sum(lis_S_I==1)
    #append the new values in the arrays
    I.append(I[i-1]-I_R+S_I)
    R.append(R[i-1]+I_R)
    S.append(S[i-1]-S_I)

#draw graph for the SIR model
plt.figure(figsize =(8,5),dpi=200)
plt.title('SIR Modle')
plt.plot(t,S,label='Susceptible')
plt.plot(t,I,label='Infected')
plt.plot(t,R,label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.legend()
plt.show()
plt.clf()