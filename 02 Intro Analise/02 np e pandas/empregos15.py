import unicodecsv
import datetime
import matplotlib.pyplot as plt
import numpy as np


employment_above_15_file = 'employment_above_15.csv'

with open(employment_above_15_file, 'rb') as f:
	reader = unicodecsv.DictReader(f)
	employments = list(reader)
    
for employment in employments:
	if employment['Country'] == 'Brazil':
		Brazil = employment
		del Brazil['Country']

#print(Brazil)
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
