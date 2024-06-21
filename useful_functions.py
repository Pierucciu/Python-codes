1# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 19:04:54 2021

@author: Roberto
"""
# This function calculate the polinomial p with coefficients coeff
def pol(x,coeff):
    y=0
    for i,a in enumerate(coeff):
        y=y+a*x**i
    return(y)

#Find the maximum and the minimum values in the list
def max_min(lis):
    k_max=lis[0]
    k_min=lis[0]
    for k in lis:
        if k>k_max:
            k_max=k
        elif k<k_min:
            k_min=k
    print(k_max,k_min)


def fibonacci(n):
    if n<=0:
        return "Error: provide an integer greater then 0 "
    else: 
        f1,f2=1,1
        for i in range(n):
            print(f1)
            f1,f2=f2,f1+f2
        
def fibonacci_recursive(n):
    if n<=0:
        return "Error: provide an integer greater then 0 "
    if n==1 or n==2:
            return 1
    else:
        return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)
        
def factorial(n):
    if n==0:
        return 1
    else:
        f=1
        for k in range(1,n+1):
            f*=k
        return(f)

def factorial_recursive(n):
    if n<=0:
        return 1
    else: 
        return n*factorial_recursive(n-1)

def binomial(n,k):
    if k==0:
        return 1
    else: 
        return int(factorial(n)/(factorial(n-k)*factorial(k)))
    
def pascal_triangle(rows):
    n=1
    while n<=rows:
        l=[]
        for k in range(n+1):
            l.append(binomial(n,k))
        print(*l)
        n+=1

# Primes factors of the integer n
def factors(n):
    factorlist=[]
    for i in range(2,n+1):
        while n%i==0:
            factorlist.append(i)
            n=n/i
    if len(factorlist)==1: 
        print("It's a prime number") 
    return factorlist

# List of the first prime numbers up to n
def primes_list(n): 
    prime_numbers=[2]
    for j in range(3,n+1):
        for k in prime_numbers:
            if j%k==0:
                break
            elif k>math.sqrt(j):
                prime_numbers.append(j)    
                break  
    print(*prime_numbers)

# Multiplication of m*p and p*n matrices 
def matrix_multipl(A,B):
    
    m,p=A.shape
    pp,n=B.shape
    if p!=pp:
        print("Error: the matrices dimension is not compatible")
    else:
        from numpy import zeros
        C=zeros([m,n]) 
        for i in range(m):
            for j in range(n):
                for k in range(p):
                    C[i,j]+=A[i,k]*B[k,j]
    return(C)

#find the highest even sum of two numbers in the same list  
def max_even_sum(filename)
    lista=open(filename,"r")
    items_number=int(lista.readline())
    lista2=lista.readline()
    items_list=list(map(int,lista2.split()))

    x_max=-1
    for i in range(items_number):
        for j in range(i+1,items_number):
            x=items_list[i]+items_list[j]
            if x%2 == 0:
                if x>x_max: x_max=x
                
    x_max=str(x_max)
    b=open("output.txt","w")
    b.write(x_max)
    b.close()
    
#find the highest even sum of two numbers in the same list optimized 

lista=open("input.txt","r")  #read the list from the file input.txt
items_number=int(lista.readline())
lista2=lista.readline()
items_list=list(map(int,lista2.split()))

x_2_even,x_max_even,x_2_odd,x_max_odd=-1,-1,-1,-1 

for x in items_list:     
        if x%2 == 0:
            if x>x_max_even: 
                    x_2_even=x_max_even
                    x_max_even=x
            elif x>x_2_even: x_2_even=x           
        else: 
            if x>x_max_odd: 
                    x_2_odd=x_max_odd
                    x_max_odd=x
            elif x>x_2_odd: x_2_odd=x

x_even=x_2_even+x_max_even

if x_even < x_max_even:    #print -1 if the evenly sum does not exist
    x_even=-1
x_odd=x_2_odd+x_max_odd
if x_odd < x_max_odd:
    x_odd=-1

x_max=max(x_even,x_odd)            
x_max=str(x_max)
b=open("output.txt","w")  #write the outcome in the file output.txt
b.write(x_max)
b.close()
