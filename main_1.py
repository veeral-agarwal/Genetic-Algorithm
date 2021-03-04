import numpy as np
from client import *
import random
#13508412130.218098 368125762698.6422
#13560827319.190525 370434930576.4746
#13532626957.355581 369745382579.87744
#13510723304.19212 368296592820.6967
f=open("overfit.txt","r")
data=f.read()
data=data.rstrip()
data=data.strip('][').split(', ')
f.close()
for i in range(len(data)):
    data[i]=float(data[i])

#print(list(data))
pop_size=10
chromosome_size=len(data)

def mod(val):
    if val<0:
        return -1*val
    return val    


# #change few genes of chromosome 
# def mutate(chromosome:np.ndarray):
#     mean=np.mean(init_pop,axis=0)
#     for i in range(chromosome_size):
#         #chromosome[i]=np.random.choice(chromosome) bad idea
#         temp=np.random.choice(mean)
#         temp=temp+random.uniform(-0.005,0.005)
#         chromosome[i]=temp
#         #if mod(temp)<mod(chromosome[i]):
#             #chromosome[i]-=temp              
# #population generation

#change few genes of chromosome 
def mutate(chromosome:np.ndarray):
    mutation_probability = 0.6
    for i in range(chromosome_size):
        l = abs(chromosome[i])/500
        r = -1*l
        temp = random.uniform(r,l)
        k = random.uniform(0,1)
        if k <= mutation_probability:
            chromosome[i]+=temp
#population generation


def get_fitness(arr, ind):
        #getting errors on the data
    fitness=[0 for i in range(chromosome_size)]
    j=0    
    for chromoso in arr:
        testerr,validerr=get_errors(key,list(chromoso))
        print(testerr,validerr)
        fitness[j]=1/(10*testerr+validerr)
        j+=1
    
    if ind==1:
        for m in range(chromosome_size):
            fitness1[m]=fitness[m]
            #print(fitness) 
    else:
        for m in range(chromosome_size):
            fitness2[m]=fitness[m]   
    #calculate probabilities
    sum_fit=np.sum(fitness)
    for k in range(pop_size):
        probability[k]=fitness[k]/sum_fit   
    #print(probability,np.sum(probability))    

def selection(arr:np.ndarray):
    for i in range(pop_size):
        parent1ind=np.random.choice(pop_size,p=probability)
        parent1=arr[parent1ind]
        parent2ind=np.random.choice(pop_size,p=probability)
        parent2=arr[parent2ind]
        new_pop[i]=crossover(parent1,parent2)

def crossover(parent1,parent2):
    mid=random.randint(1,chromosome_size-1)
    child=np.ones(chromosome_size)
    for i in range(0,mid+1):
        child[i]=parent1[i]
    for j in range(mid,chromosome_size):
        child[j]=parent2[j]
    return child

        
generations=1    
new_init_pop=np.zeros((pop_size,11))
while(generations!=5):
#at last we can put newpop to init pop and start algo again
    init_pop=np.zeros((pop_size,11))
    new_pop=np.zeros((pop_size,11))
    fitness1=[0 for i in range(chromosome_size)]
    fitness2=[0 for i in range(chromosome_size)]
    probability=[0 for j in range(pop_size)]
    #copy the original vector to all the population and change few values in the population so that it generates varied initial population,ie we can simply mutate
    for i in range(pop_size):
        if generations==1:
            init_pop[i]=list(data)
        else:
            init_pop[i]=new_init_pop[i]
        mutate(init_pop[i])
    #print(init_pop)
    get_fitness(init_pop,1)
    selection(init_pop)
    for i in range(pop_size): 
        mutate(new_pop[i])
    #print(new_pop)
    get_fitness(new_pop,2)

    #print(fitness1,"initialfitness")
    #print(fitness2,"childrenfitness")


    #we need to replace children which are more fit than parents
    #sort population according to fitness, descending

    #sorting is asc init pop indexes
    indexes_par=[j for j in range(pop_size)]
    sorted_index_par=[indexes_par for _,indexes_par in sorted(zip(fitness1,indexes_par))]
    #print(sorted_index_par)

    #sorting is asc new pop indexes
    indexes_ch=[j for j in range(pop_size)]
    sorted_index_ch=[indexes_ch for _,indexes_ch in sorted(zip(fitness2,indexes_ch))]
    #print(sorted_index_ch)

    #pick best from both()
    fitness1.sort()
    fitness2.sort()
   
    newfit=[]
    j=pop_size-1
    k=pop_size-1
    i=0
    while i!=pop_size:  
        if(fitness2[j]>fitness1[k]):
            new_init_pop[i]=new_pop[sorted_index_ch[j]]
            newfit.append(fitness2[j])
            #print("childrock",j)
            j=j-1
        
        else:
            new_init_pop[i]=init_pop[sorted_index_par[k]]
            newfit.append(fitness1[k])
            #print("fitparent",k)
            k=k-1
        i+=1
    #print(new_init_pop)
    print(newfit, "bestfit")
    generations+=1
        













 

        

