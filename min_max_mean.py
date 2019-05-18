import random
random_numbers=[]
for i in range(10):
    random_numbers.append(random.randint(10,1000))

print(random_numbers)
#for comparison
temp=random_numbers[0]

#finding maximum number
for i in range(len(random_numbers)):
    if (temp<random_numbers[i]):
         temp=random_numbers[i]

print("The maximum number in the array is : "+str(temp))

temp=random_numbers[0]

#finding minimum number
for i in range(len(random_numbers)):
    if (temp>random_numbers[i]):
         temp=random_numbers[i]

print("The minimum number in the array is : "+str(temp))


mean=0
#finding mean
for i in range(len(random_numbers)):
    mean=mean+random_numbers[i]

mean=mean/len(random_numbers)

print("The mean in the array is : "+str(mean))
    
