#import libraries
import pandas as pd 
import matplotlib.pyplot as plt 


#load dataset
data = pd.read_csv("../data/data.csv")


#Sumarry statistics
print(data.describe())


#Create a histogram of all columns
data.hist(figsize=(10,8))
plt.xticks(fontsize=8)
plt.tight_layout()
plt.show()
