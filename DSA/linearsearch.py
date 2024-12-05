a=list(map(int,input().split()))
key=int(input())
flag=0
for i in range(0,len(a)):
    if a[i]==key:
        flag=1
if flag==1:
    print("Key found")
else:
    print("key not found")