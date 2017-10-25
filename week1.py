#Text Input and Output

#Numbers
n = int(input("Enter an integer:"))
print(n)

m = float(input("Enter a decimal number:"))
print(m)

#Strings
name = input("Enter your name")
print("Welcome to my first program " + name)

print("Welcome again," , name)

#Conditions
n = int(input("Enter a number between 1 and 4:"))
if(n==1){
print("You have won 1 million dollars!")
}
elif(n==2){
print("You have won 5 million dollars!")
}
elif(n==3){
print("You haven't scored anything. Better luck next time.")
}
elif(n==4){
print("You have won the latest iPhone X!")
}
else{
print("Enter a valid number.")
}

#Variables
int a = 10;
long g = 100000;
float b = 10.0;
String name = "Anjali"
double c = 1.0000;
boolean flag = true;

int d = a + 5;
print(d) #Prints 15

int v = a+b; #Raises an error since a and b belong to different data types

#Looping
#For loops
for(int i=0; i<5; i++){
print(i)
}

n=int(input("Enter a number"))
for(int j=0; j<n; j=j+2){
print(j*j)
}

#While loops
int k = 0;
while(k<5){
a=2
b=5
a=a+b
print(a)

k=k+1
}

int n =2;
boolean flag = true;
while(flag){
n=n+1

if(n==10){
flag = false
}
}
