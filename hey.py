#! /usr/bin/python
import random
print("Enter length of binary encoding")
len = input()
len=int(len)

parent1 = []
parent2 = []
offspring = []
list1=[]
list2=[]
list3=[]
list4=[]

for i in range(len):
    x=random.randint(0,1)
    parent1.append(x)

for i in range(len):
    x=random.randint(0,1)
    parent2.append(x)

print("Parent - 1")
print(parent1)

print("Parent - 2")
print(parent2)
print("\n")




print("\nOffspring after Single point Crossover")
sp = random.randint(0,len-1)
print("Seperating point is : {0}".format(sp))

for x in range(0,sp):
    list1.append(parent1[x])

for x in range(sp,len):
    list1.append(parent2[x])

print(list1)
print("\nAfter Mutation")
for x in range(0,len):
    flo = random.uniform(0,1)
    if flo > 0.600:
        offspring.append(1-list1[x])
    else:
        offspring.append(list1[x])
print(offspring)

print("\n\n")






print("Offspring after Two point crossover")
sp1=random.randint(0,len-1)
sp2=random.randint(sp1,len-1)
print("Two Seperating points are : {0} and {1}".format(sp1,sp2))
for x in range(0,sp1):
    #print(parent1[x])
    list2.append(parent1[x])
for x in range(sp1,sp2):
    #print(parent2[x])
    list2.append(parent2[x])
for x in range(sp2,len):
    #print(parent1[x])
    list2.append(parent1[x])

print(list2)
offspring=[]
print("\nAfter Mutation")
for x in range(0,len):
    flo = random.uniform(0,1)
    if flo > 0.600:
        offspring.append(1-list2[x])
    else:
        offspring.append(list2[x])
print(offspring)
print("\n\n")




print("Offspring after Arithmetic crossover")
for x in range(0,len):
    x1=parent1[x]
    x2=parent2[x]
    if x1==1 and x2==1:
        #print("1")
        list3.append(1)
    else:
        #print("0")
        list3.append(0)
print(list3)
offspring=[]

print("\nAfter Mutation")
for x in range(0,len):
    flo = random.uniform(0,1)
    if flo > 0.600:
        offspring.append(1-list3[x])
    else:
        offspring.append(list3[x])
print(offspring)
print("\n\n")



print("Offspring after Uniform crossover")
for x in range(0,len):
    ran = random.randint(0,1)
    if ran==0:
        #print(parent1[x])
        list4.append(parent1[x])
    else:
        #print(parent2[x])
        list4.append(parent2[x])
print(list4)
offspring=[]
print("\nAfter Mutation")
for x in range(0,len):
    flo = random.uniform(0,1)
    if flo > 0.600:
        offspring.append(1-list4[x])
    else:
        offspring.append(list4[x])
print(offspring)
print("\n\n")


