import unicodecsv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


employments = pd.read_csv('employment_above_15.csv')
#print(employments['Brazil'])

employments = employments.set_index('Country')
Brazil = employments.loc('Brazil')

#for employment in employments:
#	if employment['Country'] == 'Brazil':
#		Brazil = employment
#		del Brazil['Country']

print(Brazil)
x = []
y = []
for key,value in Brazil.items():
	x.append(int(key))
	y.append(float(value))

print(y)
plt.xlabel("Anos")
plt.ylabel("Empregos")
plt.title("Empregos +15 anos - Brasil")

#plt.plot(x,y)
plt.hist(y)
plt.show()
