import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

titanic_file = 'titanic_data.csv'
titanic_data = pd.read_csv(titanic_file)



def is_data_ok(data):	
	if data['Pclass'] not in (1,2,3):
		print("Invalid Pclass ",data['Pclass'])
		return False
	if data['Sex'] not in ['male','female']:
		print("Invalid Sex ",data['Sex'])
		return False
	if math.isnan(data['Age']) or data['Age'] < 0 or data['Age'] > 120:
		print("Invalid Age ",data['Age'])
		return False
	return True

result = titanic_data.apply(is_data_ok,axis=1)
print (result.all())


mean_ages =  titanic_data.groupby(['Sex','Pclass'])['Age'].mean()


def fill_missing_ages(register):
	global mean_ages
	if math.isnan(register['Age']):
		return mean_ages[register['Sex']][register['Pclass']]
	return register['Age']

titanic_data['Age'] = titanic_data.apply(fill_missing_ages, axis=1)



result = titanic_data.apply(is_data_ok,axis=1)
print (result.all())
