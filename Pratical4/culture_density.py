#initiate the cell density ad 5
cell_density=5
#Set the starting day=1
day=0
#when the density hasn't reached 90, implement the steps below everytime
while cell_density<=90:
    #   doubles the density
    cell_density=cell_density*2
    #   add 1 to the day number
    day=day+1
#at last output the day
print("On day",day,"the cell density goes over 90%, which means you have",day-1,"free days to enjoy your holiday")
