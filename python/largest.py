list_1 = list(map(int,input().split()))
index=int(input())
temp=list_1[index]
for i in range(index+1,len(list_1)):
     if  temp < list_1[i]:
         temp=list_1[i]
print(temp)



