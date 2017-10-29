#Functions

#1. Function without parameters
def example():
    print(5)

def example2():
    a = 2
    print(a*2)

#2. Function with parameters
def example3(n1, n2):
    answer = n1+n2
    print(answer)

def example4(n1, n2, n3):
    n1=n2
    n2=n3;
    n3=n1+n2+n3
    print("First number = ", n1)
    print("Second number = ", n2)
    print("Third number = ", n3)

def example5(n1, n2):
    print(n1)
    print(n2)
    return n1+n2

x = example5(5,8)
print(x)

#3. Global Variables and Local Variables
x = 5
def example6(n1, n2):
    print(x)
    print(x+6)

y = 6
def example7(n1, n2):
    global y
    print(y)
    print(y+6)
    y+=6                  #The function works because of the declaration of y as a global variable

#Lists
A = [1,2,3,4,5,6]

#List Manipulations
A.append(9) #Adds an element 9 at the end of the List

A.insert(2,44) #Inserts an element 44 at the second index

A.remove(4) #Removes the element at the 4th index

print(A[5]) #Prints the element at the 5th index

#List Slicing
print(A[5:9]) #Prints elements starting from the 5th index uptil the 9th index (the 9th index being excluded)

print(A[4:]) #Prints all the elements starting from the 4th index upto the end of the List

print(A[:5]) #Prints all the elements uptil the 5th index (the 5th index being excluded)

print(A[:]) #Prints all the elements of the List

A.sort()
print(A) #Prints the sorted List

#Dictionaries

dict = {'Anjali':10, 'Rahul':5, 'Sumit':2, 'Mayank':-1, 'Monu':20}
print(dict)

print(dict['Sumit']) #To print a key's value

#Adding a key-value pair to a dictionary
dict['Saksham'] = 4

#Modifying a value corresponding to a key
dict['Saksham'] = 6

#Deleting a key-value pair from a dictionary
del dict['Mayank']

#Tuples

tup = (1,2,3,4)
#It is an immutable data type where elements are enclosed within roun d

print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])

#Strings

str = "abrakadabra"

print(len(s)) #Prints the length of the string

print(str[0]) #Prints the zeroth character of the string

print(str.substring(0,4)) #Prints characters of the string starting from the zeroth index uptil 4th index

print(str.upper()) #Converts all the characters of the string to uppercase

print(str.lower()) #Converts all the characters to lowercase

print(str.split(' ')) #Splits the string about the space

print(str.replace('abra','dabra')) #Replaces 'abra' with 'dabra'
