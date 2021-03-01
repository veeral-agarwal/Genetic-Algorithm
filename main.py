import numpy as np
from client import *
import random

#13510723304.19212 368296592820.6967
f=open("overfit.txt","r")
data=f.read()
data=data.rstrip()
data=data.strip('][').split(', ')
f.close()
for i in range(len(data)):
    data[i]=float(data[i])

print(list(data))
pop_size=10
chromosome_size=len(data)

def mod(val):
    if val<0:
        return -1*val
    return val    


#change few genes of chromosome 
def mutate(chromosome:np.ndarray):
    mean=np.mean(init_pop,axis=0)
    for i in range(chromosome_size):
        #chromosome[i]=np.random.choice(chromosome) bad idea
        temp=np.random.choice(mean)
        if mod(temp)<mod(chromosome[i]):
            chromosome[i]-=temp              
#population generation

def get_fitness(arr, ind):
        #getting errors on the data
    fitness=[0 for i in range(chromosome_size)]
    j=0    
    for chromoso in arr:
        testerr,validerr=get_errors("F1hP7PePw62PZ8iABBDNb2zqmkX7nbVrz8328hJ3ySZLvyQ88o",list(chromoso))
        print(testerr,validerr)
        fitness[j]=1/(10*testerr+validerr)
        j+=1
    print(fitness) 
    if ind==1:
        for m in range(chromosome_size):
            fitness1[m]=fitness[m]
    else:
        for m in range(chromosome_size):
            fitness2[m]=fitness[m]   
    #calculate probabilities
    sum_fit=np.sum(fitness)
    for k in range(pop_size):
        probability[k]=fitness[k]/sum_fit   
    print(probability,np.sum(probability))    

def selection(arr:np.ndarray):
    for i in range(pop_size):
        parent1ind=np.random.choice(pop_size,p=probability)
        parent1=arr[parent1ind]
        parent2ind=np.random.choice(pop_size,p=probability)
        parent2=arr[parent2ind]
        new_pop[i]=crossover(parent1,parent2)

def crossover(parent1,parent2):
    mid=random.randint(5,8)
    child=np.ones(chromosome_size)
    for i in range(0,mid+1):
        child[i]=parent1[i]
    for j in range(mid,chromosome_size):
        child[j]=parent2[j]
    return child

        
    

#at last we can put newpop to init pop and start algo again
init_pop=np.zeros((pop_size,11))
new_pop=np.zeros((pop_size,11))
fitness1=[0 for i in range(chromosome_size)]
fitness2=[0 for i in range(chromosome_size)]
probability=[0 for j in range(pop_size)]
#copy the original vector to all the population and change few values in the population so that it generates varied initial population,ie we can simply mutate
for i in range(pop_size):
    init_pop[i]=list(data)
    mutate(init_pop[i])
print(init_pop)
get_fitness(init_pop,1)
selection(init_pop)
for i in range(pop_size): 
    mutate(new_pop[i])
#print(new_pop)
get_fitness(new_pop,2)

print(fitness1,fitness2)


#we need to replace children which are more fit than parents
#sort population according to fitness, descending

#sorting is asc init pop indexes
indexes_par=[j for j in range(pop_size)]
sorted_index_par=[indexes_par for _,indexes_par in sorted(zip(fitness1,indexes_par))]
print(sorted_index_par)

#sorting is asc new pop indexes
indexes_ch=[j for j in range(pop_size)]
sorted_index_ch=[indexes_ch for _,indexes_ch in sorted(zip(fitness2,indexes_ch))]
print(sorted_index_ch)

#pick best from both(not done properly)
fitness1.sort(reverse=True)
fitness2.sort(reverse=True)

for i in range(pop_size):
    if fitness2[i]>fitness1[i]:
        inde=pop_size-sorted_index_ch[i]-1
        print("child rocks",inde) #take now_pop[inde] and add to next gen init pop
    else:
        inde=pop_size-sorted_index_par[i]-1
        print("parent",inde)#take init_pop[inde] and add to next gen init pop

        

