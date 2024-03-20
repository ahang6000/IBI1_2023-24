w=input("Please input the activity:")
#Prompt user to input activity and save input as variable activity
sleep=8
classes=6
study=3.5
tv=2
music=1
#Define variable sleep and assign value 8 
#Define variable classes and assign value 6
#Define variable study and assign value 3.5
#Define variable tv and assign value 2 
#Define variable music and assign value 1
Act = {"Sleeping":sleep,"Classes":classes,"Studying":study,"TV":tv,"Music":music}
#Define dictionary Act with keys "Sleeping", "Classes", "Studying", "TV", "Music" and assign values from variables
ot=24-sleep-classes-study-tv-music
#Define variable ot and calculate value as 24 minus sum of sleep, classes, study, tv, music
Act["other"]=ot
#Add key "other" to dictionary Act and assign value of variable ot
print(Act)
#Print contents of dictionary Act
print(Act[w])
#Print value of key activity from dictionary Act
import matplotlib.pyplot as plt
#Import matplotlib.pyplot library as plt
Activity_labels=list(Act.keys())
#Define list Activity_labels containing keys of dictionary Act
time=[sleep,classes,study,tv,music,ot]
#Define list time containing values of variables sleep, classes, study, tv, music, ot
plt.figure()
plt.pie(time,labels=Activity_labels)
#Create pie chart plotting values in time with labels from Activity_labels
#Set title of pie chart to "Average time"
plt.title("Average time")
#Display pie chart
plt.show()
#Clear current figure
plt.clf()
