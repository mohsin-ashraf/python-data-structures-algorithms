#declaring and initializing an array
numbers = [1,2,3,4,5]

#List numbers
print (numbers)

#We can get elements from the list in constant time if we know the index of the element.
print ("First Item of the numbers array(list): "+str(numbers[0]))

#Update the second Item
numbers[1] = 111
print ("Now the list is: "+str(numbers))

#Iterating through a python list
for number in numbers:
  print (number)

#Multiple data types in python
numbers[3] = "Mohsin"
print ("Now the list is: "+str(numbers))

#Using indices for getting items from the list
for i in range(len(numbers)):
  print (numbers[i])

#Slicing the list
print (numbers[2:4])

#Negative Slicing
print (numbers[-1])
