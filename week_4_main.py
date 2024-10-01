# #collection =single "variable" used to store multiple values 
# #list = [] ordered and changable. Duplicates OK
# #set = {} unordered and immutab;le, but add/remove OK. NO dublicates
# #tuple= () orderted and unchangable., Duplicates OK. FASTER 

# fruits = ['apple' ,  'orange' , 'banana', 'coconut', 'pineapple', 'kiwi', 'strawberry' , 'papya' , 'mango' ,]
# print (fruits[1:3])

# # list starts with 0, 0=apple, 4=put of range 

# print (len(fruits))
# # #this finds length 

# print (fruits[::2])
# # #this gives you every second word 

# print(fruits[::-1])
# # #reverses order of list 

# # for fruit in fruits:
# #first thing with itteration
# #DONT NAME VARIABLE ONE LETTER
# #fruit represent object in list 
# #itteration is looping throught the whole thing 
# #will loop through each time 
# #iteration 1- fruit = apple
# #itteration 2- fruit = orange 

# print (dir (fruits))
# #dir-gives all atributes in a list 

# # print(help(fruits))
# #gives you documentation for what it does 

# len(fruits)
# # #gives the length of the list

# print ("apple" in fruits )
#  #tells you if element is in a list
#  #boolean 
# print ("tomato " in fruits)

# #lists are ordered and changable, duplicates are ok 

# fruits[0] = "pineapple"
# #changes the value of the "0" in the list 

# fruits [2] = "grape"

# print(fruits)

# for fruit in fruits:
#     print(fruit)

# fruits.append("pineapple")
# # . append will add something to the end of the list 

# fruits.remove('grape')
# # .rempove will remove

# fruits.insert(0, 'pineapple')
# #will put that value in the given spot (pineapple in spot 1)

# fruits.sort()
# #alphabetical order

# #fruits.reverse()
# #reverse order from how you put them in 

# fruits #??
# #prints in reverse alhabetical order 

# fruits.clear()
# # ??

# print (fruits.index ('apple'))
# #finds the location/index

# for fruit in fruits:
#     print(fruit)



cars = ['ford' , 'volvo' , 'BMW']

cars.append('Honda')
cars.append('Tesla')
cars.append('Buick')
cars.append('cybertruck')
#print out as an F string 


cars[-1] = 'austin martin' 
print(f"The cars in the list are : {cars}")

#replace 3rd with another car 
cars[2] = 'suberu'
print(f"The cars in the list are : {cars}")

#insert a new car in the second position 
cars.insert(1, 'Lambo')
print(f"The cars in the list are : {cars}")

#remove 3rd element in a list 
cars.remove('volvo')
print(f"The cars in the list are : {cars}")

#check if list contains "ford" 
ford_in_cars = "ford" in cars
print (f'it is {ford_in_cars} that ford is in the list of cars ')


for car in cars:
    requestCar= input('Enter a car')
    cars.append(requestCar)
    print(f'The cars in the list are: {cars}')
    if len(cars) > 10:
        print ('you have reached max cars.')
        break 
 
for car in cars:
    print(car)