def sumofnm(x):
    if x==1:
        return 1
    elif x==0:
        return 0
    else:
        return x+sumofnm(x-1)
a=int(input())
result=sumofnm(a)
print(result)



