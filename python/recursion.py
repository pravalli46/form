def multiply(x):
    if x==1:
        return x
    else:
       return x*multiply(x-1)
x=int(input())
result=multiply(x)
print(result)
