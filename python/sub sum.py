def sum(list_x,target,list1=[]):
    for i in range(len(list_x)):
        for j in range(len(list_x)):
            if list_x[i]+list_x[j]==target:
                list1.append((list_x[i],list_x[j]))
    return list1
list_a=list(map(int,input().split()))
a=int(input())
result=sum(list_a,a)
print(result)

