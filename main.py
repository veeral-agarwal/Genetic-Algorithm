import numpy as np
from client import *
import random
import json 

#-------------------------
# f=open("overfit.txt","r")
# data=f.read()
# data=data.rstrip()
# data=data.strip('][').split(', ')
# f.close()
# for i in range(len(data)):
#     data[i]=float(data[i])
#----------------------------

with open ("TeamName1.json","r") as file:
    vectors = json.load(file)
data = vectors

#---------------------------
# data = [[]]
# for i in range(len(vectors)):
#     for j in range(len(vectors[i])):
#         data[i][j]=float(vectors[i][j])
#----------------------------

#print(list(data))
pop_size=10
chromosome_size=11
train_factor = 0.5

def mod(val):
    if val<0:
        return -1*val
    return val    

#change few genes of chromosome 
def mutate(chromosome:np.ndarray):
    mutation_probability = 0.2
    for i in range(chromosome_size):
        l = abs(chromosome[i])/5000
        r = -1*l
        temp = random.uniform(r,l)
        k = random.uniform(0,1)
        if k <= mutation_probability:
            chromosome[i]+=temp
        if chromosome[i]>10:
            chromosome[i]=10
        elif chromosome[i]<-10:
            chromosome[i]=-10

#population generation

def get_fitness(arr, ind):
        #getting errors on the data
    fitness=[0 for i in range(chromosome_size)]
    j=0    
    for chromoso in arr:
        testerr,validerr=get_errors(key,list(chromoso))
        print(testerr,validerr)
        fitness[j]=1/(train_factor*testerr+validerr)
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

        #printing parents after selection :
        print("printing parents after selection :")
        print("parent1:")
        print(parent1)
        print("parent2:")
        print(parent2)

        new_pop[i]=crossover(parent1,parent2)

def crossover(parent1,parent2):
    mid=random.randint(1,chromosome_size-1)
    child=np.ones(chromosome_size)
    for i in range(0,mid+1):
        child[i]=parent1[i]
    for j in range(mid,chromosome_size):
        child[j]=parent2[j]
    print(child)
    return child


# temp_arr  = np.zeros((pop_size,11))
temp_arr = data
print(temp_arr)

        
generations=1
new_init_pop=np.zeros((pop_size,11))
while(generations!=21):

    #at last we can put newpop to init pop and start algo again
    init_pop=np.zeros((pop_size,11))
    new_pop=np.zeros((pop_size,11))
    fitness1=[0 for i in range(chromosome_size)]
    fitness2=[0 for i in range(chromosome_size)]
    probability=[0 for j in range(pop_size)]
    
    # init_pop = new_init_pop

    #copy the original vector to all the population and change few values in the population so that it generates varied initial population,ie we can simply mutate
    for i in range(pop_size):
        # if generations==1:
        #     init_pop[i]=list(data)
            # for i in range (n):
            # rng = np.random.uniform(low = -0.30, high = 0.30, size=(1, 11))
            # init_pop [i, :] = list(data) + rng* list(data)
        
        if generations==0:
    
            # init_pop[i]=list(data)

            # for j in range(chromosome_size):
            #     init_pop[i][j]=0

            for j in range (chromosome_size):

                tempp = random.randint(1,10)
                if tempp < 8:
                    rng = np.random.uniform(low = 0.3, high = 0.80)
                    
                    init_pop[i][j] = rng* temp_arr[i][j]
        
        else:

            for j in range (chromosome_size):
                # tempp = random.randint(1,10)
                # if tempp < 8:
                    # rng = np.random.uniform(low = 0.3, high = 0.80)
                init_pop[i][j] = temp_arr[i][j]
            # init_pop[i]=new_init_pop[i]
        mutate(init_pop[i])
    
    #initial population printing
    print("initial population :")
    for lol in init_pop:
        print(lol)

    get_fitness(init_pop,1)
    selection(init_pop)
    
    # printing population after crossover
    print("after crossover:")
    for lol in new_pop:
        print(lol)

    # mutation
    for i in range(pop_size): 
        mutate(new_pop[i])

    #printing population after mutation
    print("population after mutation :")
    for lol in new_pop:
        print(lol)

    #print(new_pop)
    get_fitness(new_pop,2)

    #print(fitness1,"initialfitness")
    #print(fitness2,"childrenfitness")


    #we need to replace children which are more fit than parents
    #sort population according to fitness, descending

    #new_init_pop=np.zeros()
    finaltup=[]
    for i in range(pop_size):
        finaltup.append((fitness1[i],init_pop[i]))
    
    for i in range(pop_size):
        finaltup.append((fitness2[i],new_pop[i]))
    print("final touple:")
    print(finaltup)

    finaltup.sort(reverse=True , key=lambda x:x[0])

    print("final sorted touple")
    print(finaltup)
    print("FFS , MIXED FITNESS FUNCTIONS IN ORDER")
    for i in range(pop_size):
        new_init_pop[i]=finaltup[i][1]
        print(finaltup[i][0])

    ret=submit(key,list(new_init_pop[0]))  
    print(ret)

    #printing the vector we are submitting
    print("the vector we are submitting",end=" ")
    print(new_init_pop[0])

    tr ,va = get_errors(key,list(new_init_pop[0]))

    update = []
    for i in range(len(new_init_pop)):
        update.append(list(new_init_pop[i]))

    loll = open("9mar_vector.txt","a")
    loll.write(str(new_init_pop[0] )+"\n")
    loll.close()

    loll = open("9mar_tr.txt","a")
    loll.write(str(tr  )+"\n")
    loll.close()

    loll = open("9mar_va.txt","a")
    loll.write(str(va )+"\n")
    loll.close()

    generations+=1

with open('TeamName1.json','w') as outfile:
    json.dump(update,outfile)

