from client import *
import numpy as np
import random

f=open("overfit.txt","r")
data=f.read()
data=data.rstrip()
data=data.strip('][').split(', ')
f.close()
for i in range(len(data)):
    data[i]=float(data[i])

pop_size=10
radiation=2.5

population=np.zeros((pop_size,11))
new_population=np.zeros((pop_size,11))
fitness=np.zeros((pop_size))
new_fitness=np.zeros((pop_size))
probability=np.zeros((pop_size))
indices=np.zeros((pop_size))
for i in range(pop_size):
    population[i]=list(data)
    indices[i]=i


for i in range(1):
    training,validation=get_errors("F1hP7PePw62PZ8iABBDNb2zqmkX7nbVrz8328hJ3ySZLvyQ88o",population[i].tolist())
    print(training,validation)
