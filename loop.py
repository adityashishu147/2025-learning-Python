
#for loop

fruits = ['apple' , 'banana' , 'cherry']
for x in fruits:
    print(x)


#while loop

count = 0
while count <5:   #run till i
    print(count)
    count += 1


#break

for i in range(100):
    if i == 5 :
        break
    print (i)

#countinue

for i in range(100):
    if i == 5 : #it will skip the current condition
        continue 
    print (i)

#looping through dictionary

person ={"name": "Aditya" , "age":"20" , "city": "Bangalore"}

for key,value in person.items():
    print (key,value)
    print (f'{key}:{value}')

#loop control with else

for i in range(5):
    print(i)

else:
    print("loop completed without break")

for i in range(5):
    if i == 3:
        break
    print(i)

else:
    print("loop completed")



