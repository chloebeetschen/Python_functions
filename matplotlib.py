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
plt.xticks(br1, years)
plt.legend()



#scatterplot
fig2 = plt.subplots(figsize =(6, 4)) 
plt.scatter(men, years, c ="blue", marker = 'x')
plt.scatter(women, years, c ="pink")
plt.xlabel('Year', fontweight ='bold', fontsize = 11) 
plt.ylabel('Percentage', fontweight ='bold', fontsize = 11) 


plt.legend()
plt.show
plt.show
