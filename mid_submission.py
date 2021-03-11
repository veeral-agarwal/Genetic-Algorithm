
# import numpy as np
# from client import *
# import random
# #13508412130.218098 368125762698.6422
# #13560827319.190525 370434930576.4746
# #13532626957.355581 369745382579.87744
# #13510723304.19212 368296592820.6967   this
# f=open("overfit.txt","r")
# data=f.read()
# data=data.rstrip()
# data=data.strip('][').split(', ')
# f.close()


# flag = 0


# for i in range(len(data)):
#     data[i]=float(data[i])



# #print(list(data))
# pop_size=10
# chromosome_size=len(data)
# train_factor = 0.5

# def mod(val):
#     if val<0:
#         return -1*val
#     return val    


# #change few genes of chromosome 
# '''
# def mutate(chromosome:np.ndarray):
#     mean=np.mean(init_pop,axis=0)
#     for i in range(chromosome_size):
#         #chromosome[i]=np.random.choice(chromosome) bad idea
#         temp=np.random.choice(mean)
#         #temp=temp+random.uniform(-0.005,0.005)
#         #chromosome[i]=temp
#         if mod(temp)<mod(chromosome[i]):
#             chromosome[i]-=temp              
# #population generation
# '''

# '''def get initial pop (n = population): population = np.zeros (shape (n, 11))

# for i in range (n):

# rng = np.random.uniform(low = -0.30, high = 0.30, size=(1, 11))

# #rng = np. random.uniform(low = 0.15, high = 0.15, size=(1, 11)) population [i, :] = overfit_vector + png overfit vector

# return population'''




# #change few genes of chromosome 
# def mutate(chromosome:np.ndarray):
#     mutation_probability = 0.4
#     for i in range(chromosome_size):
#         l = abs(chromosome[i])/5000
#         r = -1*l
#         temp = random.uniform(r,l)
#         k = random.uniform(0,1)
#         if k <= mutation_probability:
#             chromosome[i]+=temp
#         if chromosome[i]>10:
#             chromosome[i]=10
#         elif chromosome[i]<-10:
#             chromosome[i]=-10
# #population generation

# def get_fitness(arr, ind):
#         #getting errors on the data
#     fitness=[0 for i in range(chromosome_size)]
#     j=0    
#     for chromoso in arr:
#         testerr,validerr=get_errors(key,list(chromoso))
#         print(testerr,validerr)
#         fitness[j]=1/(train_factor*testerr+validerr)
#         j+=1
    
#     if ind==1:
#         for m in range(chromosome_size):
#             fitness1[m]=fitness[m]
#             #print(fitness) 
#     else:
#         for m in range(chromosome_size):
#             fitness2[m]=fitness[m]   
#     #calculate probabilities
#     sum_fit=np.sum(fitness)
#     for k in range(pop_size):
#         probability[k]=fitness[k]/sum_fit   
#     #print(probability,np.sum(probability))    

# def selection(arr:np.ndarray):
#     for i in range(pop_size):
#         parent1ind=np.random.choice(pop_size,p=probability)
#         parent1=arr[parent1ind]
#         parent2ind=np.random.choice(pop_size,p=probability)
#         parent2=arr[parent2ind]

#         #printing parents after selection :
#         print("printing parents after selection :")
#         print("parent1:")
#         print(parent1)
#         print("parent2:")
#         print(parent2)

#         new_pop[i]=crossover(parent1,parent2)

# def crossover(parent1,parent2):
#     mid=random.randint(1,chromosome_size-1)
#     child=np.ones(chromosome_size)
#     for i in range(0,mid+1):
#         child[i]=parent1[i]
#     for j in range(mid,chromosome_size):
#         child[j]=parent2[j]
#     return child



# temp_arr  = np.zeros((pop_size,11))
# temp_arr = list(data)
# print(temp_arr)


# generations=1
# new_init_pop=np.zeros((pop_size,11))
# while(generations!=11):
# #at last we can put newpop to init pop and start algo again
#     init_pop=np.zeros((pop_size,11))
#     new_pop=np.zeros((pop_size,11))
#     fitness1=[0 for i in range(chromosome_size)]
#     fitness2=[0 for i in range(chromosome_size)]
#     probability=[0 for j in range(pop_size)]
    
#     if flag == 1:
#         pass
#     print(init_pop)

#     #copy the original vector to all the population and change few values in the population so that it generates varied initial population,ie we can simply mutate
#     for i in range(pop_size):
#         if generations==1:

#             # init_pop[i]=list(data)

#             # for j in range(chromosome_size):
#             #     init_pop[i][j]=0

#             if flag == 0:
#                 for j in range (chromosome_size):

#                     tempp = random.randint(1,10)
#                     if tempp < 8:
#                         rng = np.random.uniform(low = 0.3, high = 0.80)
                        
#                         init_pop[i][j] = rng* temp_arr[j]
        
        
#         else:
#             init_pop[i]=new_init_pop[i]
#         mutate(init_pop[i])
    
#     #initial population printing
#     print("initial population :")
#     for lol in init_pop:
#         print(lol)
#     # generations+=1


#     get_fitness(init_pop,1)
#     selection(init_pop)
    
#     # printing population after crossover
#     print("after crossover:")
#     for lol in new_pop:
#         print(lol)

#     # mutation
#     for i in range(pop_size): 
#         mutate(new_pop[i])

#     #printing population after mutation
#     print("population after mutation :")
#     for lol in new_pop:
#         print(lol)
#     print(new_pop)

#     #print(new_pop)
#     get_fitness(new_pop,2)

#     #print(fitness1,"initialfitness")
#     #print(fitness2,"childrenfitness")


#     #we need to replace children which are more fit than parents
#     #sort population according to fitness, descending
#     '''
#     #sorting is asc init pop indexes
#     indexes_par=[j for j in range(pop_size)]
#     sorted_index_par=[indexes_par for _,indexes_par in sorted(zip(fitness1,indexes_par))]
#     #print(sorted_index_par)

#     #sorting is asc new pop indexes
#     indexes_ch=[j for j in range(pop_size)]
#     sorted_index_ch=[indexes_ch for _,indexes_ch in sorted(zip(fitness2,indexes_ch))]
#     #print(sorted_index_ch)

#     #pick best from both()
#     #fitness1.sort()
#     #fitness2.sort()
#     '''
#     #new_init_pop=np.zeros()
#     finaltup=[]
#     for i in range(pop_size):
#         finaltup.append((fitness1[i],init_pop[i]))
    
#     for i in range(pop_size):
#         finaltup.append((fitness2[i],new_pop[i]))
#     finaltup.sort(reverse=True)
#     print("FFS , MIXED FITNESS FUNCTIONS IN ORDER")
#     for i in range(pop_size):
#         new_init_pop[i]=finaltup[i][1]
#         print(finaltup[i][0])
#     ret=submit(key,list(new_init_pop[0]))  
#     print(ret)

#     #printing the vector we are submitting
#     print("the vector we are submitting",end=" ")
#     print(new_init_pop[0])
 
#     generations+=1






# '''


# generation 2:

# [ 0.00000000e+00  0.00000000e+00 -1.56537120e-13  2.68797954e-11
#  -5.82183156e-11  0.00000000e+00  0.00000000e+00  1.07994644e-05
#   0.00000000e+00 -5.55716568e-09  0.00000000e+00]
# [ 0.00000000e+00 -1.14741636e-12 -1.73187588e-13  2.68798933e-11
#  -5.82183156e-11 -7.16923843e-16  2.59822851e-16  0.00000000e+00
#  -8.85989218e-07  0.00000000e+00  3.69635474e-10]
# [ 0.00000000e+00  0.00000000e+00 -1.56552289e-13  2.68797954e-11
#  -5.82241318e-11 -7.16923843e-16  5.00487193e-16  1.79048220e-05
#  -1.28396813e-06 -5.19317248e-09  3.97301505e-10]
# [ 0.00000000e+00 -8.20893827e-13 -1.29424387e-13  2.20384261e-11
#  -8.32068751e-11  0.00000000e+00  0.00000000e+00  1.07980816e-05
#   0.00000000e+00 -9.47379294e-09  5.66012064e-10]
# [ 0.00000000e+00 -6.07972045e-13 -1.56552289e-13  2.68797954e-11
#  -5.82183156e-11 -7.16923843e-16  2.59822851e-16  0.00000000e+00
#  -8.85968069e-07  0.00000000e+00  3.69577340e-10]
# [ 0.00000000e+00 -8.20778816e-13 -1.29423512e-13  2.20344546e-11
#  -8.32023599e-11  0.00000000e+00  0.00000000e+00  1.07980816e-05
#   0.00000000e+00 -5.55716568e-09  5.65989288e-10]
# [ 0.00000000e+00 -6.07972045e-13 -8.42952997e-14  3.30498402e-11
#   0.00000000e+00 -7.16860487e-16  2.59859324e-16  0.00000000e+00
#  -8.85684818e-07  0.00000000e+00  3.69635474e-10]
# [ 0.00000000e+00  0.00000000e+00 -1.56526130e-13  2.68797954e-11
#  -5.82183156e-11 -7.16918132e-16  5.00512881e-16  1.79015709e-05
#  -1.28429180e-06 -5.19197834e-09  3.97235508e-10]
# [ 0.00000000e+00  0.00000000e+00 -1.56553882e-13  2.68797954e-11
#  -5.82192403e-11 -7.16923843e-16  2.59822851e-16  0.00000000e+00
#  -8.85836093e-07  0.00000000e+00  3.69635474e-10]
# [ 0.00000000e+00  0.00000000e+00 -1.56541696e-13  2.68797954e-11
#  -5.82183156e-11  0.00000000e+00  0.00000000e+00  1.07980816e-05
#   0.00000000e+00 -5.55716568e-09  0.00000000e+00]




# '''




# ------------------------------------------------------------------------------------

import numpy as np
from client import *
import random
import json 
#13508412130.218098 368125762698.6422
#13560827319.190525 370434930576.4746
#13532626957.355581 369745382579.87744
#13510723304.19212 368296592820.6967   this
# f=open("overfit.txt","r")
# data=f.read()
# data=data.rstrip()
# data=data.strip('][').split(', ')
# f.close()
# for i in range(len(data)):
#     data[i]=float(data[i])


with open ("TeamName1.json","r") as file:
    vectors = json.load(file)
# data = [[]]
# for i in range(len(vectors)):
#     for j in range(len(vectors[i])):
#         data[i][j]=float(vectors[i][j])

data = vectors

#print(list(data))
pop_size=10
chromosome_size=11
train_factor = 0.5

def mod(val):
    if val<0:
        return -1*val
    return val    


#change few genes of chromosome 
'''
def mutate(chromosome:np.ndarray):
    mean=np.mean(init_pop,axis=0)
    for i in range(chromosome_size):
        #chromosome[i]=np.random.choice(chromosome) bad idea
        temp=np.random.choice(mean)
        #temp=temp+random.uniform(-0.005,0.005)
        #chromosome[i]=temp
        if mod(temp)<mod(chromosome[i]):
            chromosome[i]-=temp              
#population generation
'''

'''def get initial pop (n = population): population = np.zeros (shape (n, 11))

for i in range (n):

rng = np.random.uniform(low = -0.30, high = 0.30, size=(1, 11))

#rng = np. random.uniform(low = 0.15, high = 0.15, size=(1, 11)) population [i, :] = overfit_vector + png overfit vector

return population'''




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
        # appending parents after selection in generation file 
        generation_file.write("parents after selection:\n")
        generation_file.write("parent1 and its probability : ")
        generation_file.write(str(parent1)+str(probability[parent1ind])+"\n")
        generation_file.write("parent2 and its probability:  ")
        generation_file.write(str(parent2)+str(probability[parent2ind])+"\n")
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

        

generation_file = open("11mar_generations.txt","a")

generations=1
new_init_pop=np.zeros((pop_size,11))
while(generations!=2):
#at last we can put newpop to init pop and start algo again
    init_pop=np.zeros((pop_size,11))
    new_pop=np.zeros((pop_size,11))
    fitness1=[0 for i in range(chromosome_size)]
    fitness2=[0 for i in range(chromosome_size)]
    probability=[0 for j in range(pop_size)]
    
    
    #copy the original vector to all the population and change few values in the population so that it generates varied initial population,ie we can simply mutate
    for i in range(pop_size):
        # if generations==1:
        #     init_pop[i]=list(data)
            # for i in range (n):
            # rng = np.random.uniform(low = -0.30, high = 0.30, size=(1, 11))
            # init_pop [i, :] = list(data) + rng* list(data)
        
        if generations==1:
    
            # init_pop[i]=list(data)

            # for j in range(chromosome_size):
            #     init_pop[i][j]=0

            for j in range (chromosome_size):

                tempp = random.randint(1,10)
                if tempp < 8:
                    rng = np.random.uniform(low = 0.3, high = 0.80)
                    
                    init_pop[i][j] = rng* temp_arr[i][j]
        
        else:
            init_pop[i]=new_init_pop[i]
        mutate(init_pop[i])
    
    #initial population printing
    print("initial population :")
    for lol in init_pop:
        print(lol)
    #appending initial population in generations file
    generation_file.write("\n \n \n \ngeneration 1 \n\n") #put here generation number
    generation_file.write("initial population:\n")
    for lol in init_pop:
        generation_file.write(str(lol)+"\n")
    generation_file.write("\n")
    # generations+=1


    get_fitness(init_pop,1)
    selection(init_pop)
    
    # printing population after crossover
    print("after crossover:")
    for lol in new_pop:
        print(lol)
    # appending population after crossover in generation file 
    generation_file.write("population after corssover:\n")
    for lol in new_pop:
        generation_file.write(str(lol)+"\n")
    generation_file.write("\n")

    # mutation
    for i in range(pop_size): 
        mutate(new_pop[i])

    #printing population after mutation
    print("population after mutation :")
    for lol in new_pop:
        print(lol)
    # appending population after mutation in generation file 
    generation_file.write("population after mutation:\n")
    for lol in new_pop:
        generation_file.write(str(lol)+"\n")
    generation_file.write("\n")



    #print(new_pop)
    get_fitness(new_pop,2)

    #print(fitness1,"initialfitness")
    #print(fitness2,"childrenfitness")


    #we need to replace children which are more fit than parents
    #sort population according to fitness, descending
    '''
    #sorting is asc init pop indexes
    indexes_par=[j for j in range(pop_size)]
    sorted_index_par=[indexes_par for _,indexes_par in sorted(zip(fitness1,indexes_par))]
    #print(sorted_index_par)

    #sorting is asc new pop indexes
    indexes_ch=[j for j in range(pop_size)]
    sorted_index_ch=[indexes_ch for _,indexes_ch in sorted(zip(fitness2,indexes_ch))]
    #print(sorted_index_ch)

    #pick best from both()
    #fitness1.sort()
    #fitness2.sort()
    '''
    #new_init_pop=np.zeros()
    finaltup=[]
    for i in range(pop_size):
        finaltup.append((fitness1[i],init_pop[i]))
    
    for i in range(pop_size):
        finaltup.append((fitness2[i],new_pop[i]))
    print("final touple:")
    print(finaltup)
# <<<<<<< HEAD
    finaltup.sort(reverse=True , key=lambda x:x[0])
# =======
    finaltup.sort(reverse=True, key=lambda x:x[0]) #made change here
# >>>>>>> 79663dab7f777da52388a064f057b1a35a525a35
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




    loll = open("vector1.txt","a")
    loll.write(str(new_init_pop[0] ))
    loll.close()

    loll = open("tr1.txt","a")
    loll.write(str(tr  )+"\n")
    loll.close()

    loll = open("va1.txt","a")
    loll.write(str(va )+"\n")
    loll.close()


    generations+=1


with open('TeamName1.json','w') as outfile:
    json.dump(update,outfile)



'''
[ 0.00000000e+00 -1.45791987e-12 -2.28980078e-13  4.62026183e-11
 -1.75232807e-10 -1.83669770e-15  8.52944060e-16  2.29423303e-05
 -2.04721003e-06 -1.59784330e-08  9.98380485e-10]
[ 0.00000000e+00 -1.45791987e-12 -2.28980078e-13  4.62165370e-11
 -1.75214813e-10 -1.83669770e-15  8.52944060e-16  2.29423303e-05
 -2.04726501e-06 -1.59792834e-08  9.98289696e-10]
[ 0.00000000e+00 -1.45799022e-12 -2.28980078e-13  4.62094809e-11
 -1.75240463e-10 -1.83689245e-15  8.52944060e-16  2.29423303e-05
 -2.04726501e-06 -1.59792834e-08  9.98172827e-10]
[ 0.00000000e+00 -1.45799022e-12 -2.28980078e-13  4.62010753e-11
 -1.75214358e-10 -1.83695504e-15  8.52944060e-16  2.29423303e-05
 -2.04713431e-06 -1.59792834e-08  9.98214034e-10]
[ 0.00000000e+00 -1.45799022e-12 -2.28980078e-13  4.62010753e-11
 -1.75214813e-10 -1.83705704e-15  8.52993038e-16  2.29424118e-05
 -2.04717969e-06 -1.59818356e-08  9.98214034e-10]
[ 0.00000000e+00 -1.45823003e-12 -2.28980078e-13  4.62010753e-11
 -1.75214813e-10 -1.83669770e-15  8.52944060e-16  2.29474725e-05
 -2.04732743e-06 -1.59792834e-08  9.98214034e-10]
[ 0.00000000e+00 -1.45791987e-12 -2.28954113e-13  4.62090729e-11
 -1.75214813e-10 -1.83669770e-15  8.52944060e-16  2.29388125e-05
 -2.04740215e-06 -1.59784330e-08  9.98386710e-10]
[ 0.00000000e+00 -1.45802904e-12 -2.28980078e-13  4.62094809e-11
 -1.75240463e-10 -1.83689245e-15  8.52944060e-16  2.29467194e-05
 -2.04686387e-06 -1.59777469e-08  9.98214034e-10]
[ 0.00000000e+00 -1.45810044e-12 -2.28980250e-13  4.62010753e-11
 -1.75232807e-10 -1.83669770e-15  8.52944060e-16  2.29423303e-05
 -2.04748606e-06 -1.59784330e-08  9.98153221e-10]
[ 0.00000000e+00 -1.45792140e-12 -2.28954583e-13  4.62094809e-11
 -1.75255822e-10 -1.83669770e-15  8.52944060e-16  2.29423303e-05
 -2.04740927e-06 -1.59789814e-08  9.98501919e-10]
'''


'''
[ 0.00000000e+00 -1.45791987e-12 -2.28980078e-13  4.62026183e-11
 -1.75232807e-10 -1.83669770e-15  8.52944060e-16  2.29423303e-05
 -2.04721003e-06 -1.59784330e-08  9.98380485e-10]

the vector we are submitting [ 0.00000000e+00 -4.68244455e-13 -1.23800807e-13  4.62010753e-11
 -1.08897836e-10 -1.83645233e-15  2.85985980e-16  2.29457065e-05
 -2.04721003e-06 -5.09817427e-09  6.19031957e-10]

'''
