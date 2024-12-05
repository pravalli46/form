'''def square_of_number(num):
    L=[]
    for i in num:
         square=int(i)**2
         L.append(square)
    return L

num=input()
result=square_of_number(num)
print(result)'''
a=list(map(int,input().split()))
L=[]
for i in a:
    b=int(i)**2
    L.append(b)
c=sorted(L)
print(c)


