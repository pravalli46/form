'''def factorial(n):
   if n==0 or n==1:
        return 1
   else:
        return n*factorial(n-1)'''

def factorial(n):
    sum=0
    for i in range(1,n+1):
        sum+=factorial(i)
    return(sum)
n=int(input())
result=factorial(n)
print(result)
sum_result=factorial(n)
print(sum_result)

'''def fibanocii(n):
    L=[]
    a,b=0,1
    for _ in range(n):
       L.append(a)
       a,b=b,a+b
    return L
n=int(input())
result=fibanocii(n)
print(result)'''

'''def prime_number(n):

    for i in range(2,n):
        if n%i!=0:
            return"prime"
        else:
            return "not a prime"
n=int(input())
result=prime_number(n)
print(result)'''

#palindrome madam
'''def palindrome(n):
    for i in n:
        if n==n[::-1]:
            return "palindrome"
        else:
            return "not a palindrome"
n=input()
result=palindrome(n)
print(result)'''

'''def multiplication_table(num):
    for i in range(1,11):
        print (f"{num}x{i}={num*i}")
n=int(input())
multiplication_table(n)'''
#farenheit=(celsius*9/5)+32
#celsius=(fareheit-32)*5/9

'''def bubble_sort(n):
    a=len(n)
    for i in range(a):
        for j in range(0,a-1):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j] 
    print(n)
n=list(map(int,input().split()))                  
bubble_sort(n)'''

'''def count_vowels(n):
    count=0
    for i in n:
        if i in "aeiouAEIOU":
            count+=1
    return count
n=input()
result=count_vowels(n)
print(result)'''

'''def lcm(a,b):
    num=max(a,b)
    while True:
        if num%a==0 and num%b==0:
            lc=num
            break
        num=num+1
    return lc
a=int(input())
b=int(input())
result=lcm(a,b)
print(result)'''

# Anagram listen,silent
'''def anagram(n1,n2):
    s1=sorted(n1)
    s2=sorted(n2)
    if s1==s2:
        print("anagram")
    else:
        print("not an anagram")
n1=input()
n2=input()
anagram(n1,n2)'''
#Binary search
'''def binary_search(L,target):
    a=len(L)
    beg,end=0,a-1
    while beg<=end:
        mid=(beg+end)//2
        if L[mid]==target:
            return mid
        elif L[mid]<target:
            beg=mid+1
        else:
            end=mid-1
    return -1
L=list(map(int,input().split()))
target=int(input())
res=binary_search(L,target)
if res!=1:
    print("element is present")
else:
    print("element is not found")'''
#Armstrong Number
'''def armstrong_number(n):
    sum=0
    for i in n:
        sum=sum+int(i)**3
    return sum
n=input()
result=armstrong_number(n)
print(result)'''
#Linear search
'''def linear_search(L,target):
    for i in range(len(L)):
        if L[i]==target:
            return"element found"
        
    return "not found"
L=list(map(int,input().split()))
target=int(input())
res=linear_search(L,target)
print(res)'''
#gcd
'''import math
def gcd(a,b):
    return math.gcd(a,b)
a=int(input())
b=int(input())
res=gcd(a,b)
print(res)'''
#perfect number
'''def perfect_number(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum==n:
         return "perfect num"
    else:
        return "not a perfect num"
n=int(input())
res=perfect_number(n)
print(res)'''
#perfect sqaure
def perfect_square(n):
    if n<0:
        return False
    sqrt_num=int(n**0.5)
    return sqrt_num*sqrt_num==n
n=int(input())
res=perfect_square(n)
print(res)

        

