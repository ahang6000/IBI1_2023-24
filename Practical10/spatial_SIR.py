import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
population = np.zeros((100,100))
#choose a infection point
outbreak = np.random.choice(range(100),2)
population[outbreak[0], outbreak[1]] = 1
#draw the initial image
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
#set the variables
beta=0.3
gamma=0.05
m=outbreak[0]
n=outbreak[1]

# define a function to choose the eight neighbors around the infected point
def get_neighbors(x, y):
    x_min, x_max = max(0, x - 1), min(population.shape[0] - 1, x + 1)
    y_min, y_max = max(0, y - 1), min(population.shape[1] - 1, y + 1)
    return np.array([[i, j] for i in range(x_min, x_max + 1) for j in range(y_min, y_max + 1) if (i, j) != (x, y)])

#loop 100 times
for t in range(0,100):
    for x in range(0,100):
        for y in range(0,100):
            #for the points that are infected, they can infect their neighbors and recover
            if population[x,y]==1:
                infecting_neighbors= get_neighbors(x,y)
                for i,j in infecting_neighbors:
                    #if the neighbors are susceptible, randomly infect them
                    if population[i,j]==0:
                        if np.random.choice([True,False],p=[beta,1-beta]):
                            population[i,j]=1
                #whether the infected point will recover
                if np.random.choice([True,False], p=[gamma,1-gamma]):
                    population[x,y]=2
    plt.clf()
    plt.imshow(population, cmap='viridis', interpolation='nearest')
    plt.title(f'Time {t+1}')
    plt.pause(0.03)
plt.pause(3)
plt.clf()