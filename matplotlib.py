#imports
import matplotlib.pyplot as plt
import numpy as np


labels = ['% men', '% women']
men = [15.1, 28.3]
women = [25.2, 30.0]
years = [2010, 2011]

#bar chart
barWidth = 0.4
fig = plt.subplots(figsize =(4, 6)) 

# Set position of bar on X axis 
br1 = np.arange(len(years)) 
br2 = [x + barWidth for x in br1] 

# Make the plot
plt.bar(br1, men, color ='b', width = barWidth, label ='% men') 
plt.bar(br2, women, color ='pink', width = barWidth, label ='% women') 

# Adding Xticks 
plt.xlabel('Year', fontweight ='bold', fontsize = 11) 
plt.ylabel('Percentage', fontweight ='bold', fontsize = 11) 
#plt.xticks([r + barWidth for r in range(len(men))], years)
plt.xticks(br1, years) 

#scatterplot
plt.scatter(br1, men, women, years)
plt.xlabel('Year', fontweight ='bold', fontsize = 11) 
plt.ylabel('Percentage', fontweight ='bold', fontsize = 11) 


plt.legend()
plt.show
