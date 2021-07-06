import pandas as pd 

import matplotlib.pyplot as plt 


#load dataset
data = pd.read_csv("../data/data.csv")


#Sumarry statistics
print(data.describe())

n=max(data['Salary'])
#Create a histogram of all columns
range = (0, n) 
bins = 10  
  
# plotting a histogram 
plt.hist(data['Salary'], bins, range, color = 'green', 
        histtype = 'bar', rwidth = 0.8) 
plt.xlabel('Salary')
plt.ylabel('frequency')
plt.xticks(fontsize=8)
plt.tight_layout()
plt.show()
