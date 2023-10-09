#imports
import matplotlib.pyplot as plt
import numpy as np


labels = ['% men', '% women']
men = [15.1, 25.2]
women = [28.3, 30.0]
years = [2010, 2011]

#bar chart
barWidth = 0.4
fig = plt.subplots(figsize =(6, 4)) 

# Set position of bar on X axis 
x = np.arange(2) 

# Make the plot

plt.bar(x-0.2, men, color ='blue', width = barWidth, label ='% men') 
plt.bar(x+0.2, women, color ='pink', width = barWidth, label ='% women') 

# Adding Xticks
plt.xlabel('Year', fontweight ='bold', fontsize = 11) 
plt.ylabel('Percentage', fontweight ='bold', fontsize = 11) 
plt.xticks(x, years)
plt.legend()



#scatterplot

labels = ['% men', '% women']
men = [15.1, 25.2]
women = [28.3, 30.0]
years = ["2010", "2011"]

fig2 = plt.subplots(figsize =(6, 4)) 
plt.scatter(years, men, c ="blue", marker ="x")
plt.scatter(years, women, c ="pink")
plt.xlabel('Year', fontweight ='bold', fontsize = 11) 
plt.ylabel('Percentage', fontweight ='bold', fontsize = 11) 
plt.xticks(x, years)
plt.legend()


plt.legend(['% men', '% women'])
plt.show
