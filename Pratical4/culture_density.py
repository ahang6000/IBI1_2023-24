#define variables
cd=5
hd=1
#cd=>cell density, hd=holiday days
#use for loop to adding up days
while cd<=90:
	hd+=1
	cd=2*cd
hd=str(hd)
#output the answer
print("on the "+hd+" day the cell density goes over 90%, which is the maximum number of days you can have a holiday from lab ")
