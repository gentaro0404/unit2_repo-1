#2022-11-22 Quiz 028

#Create a graoh for the X and Y values below

data = {'x':[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],'y':[24,1,2,25,26,21,23,34,49,2,19,32,7,17,36,7,45,28,40,46]}

import matplotlib.pyplot as plt

plt.plot(data['x'],data['y'], color="red", marker="o")

#Add item to dictionary
data['title'] = "quiz028"

plt.title(data['title'])
plt.xlabel("x")
plt.ylabel("y")
plt.show()