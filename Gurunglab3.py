#Sanjay Gurung session 2

def list_prime(n):
    
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j==0:
                break
            else:
                print(i)
                break
 


import math
n= int(input("Enter a number to get a prime factor of: "))
print("Prime factors are:")
while(n%2)==0:
    print(2)
    n=n//2

for i in range(3,n+1):
    while(n%i)==0:
        print(i)
        n=n//i

if n>2:
    print(n)



def convert_grade(n):
    if n>=0 and n<40:
        print("F")
    elif n>=40 and n<60:
        print("D")
    elif n>=60 and n<80:
        print("C")
    elif n>=80 and n<90:
        print("B")
    else:
        print("A")




import math
n= int(input("Enter a number for The Collatz Conjeture Sequence of:"))
while (True):
    if n % 2==0:
        n=n//2
        print(n)
    else :
        n=3*n+1
        print(n)
    if(n==1):
        break

