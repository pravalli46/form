def sum_of_odd_numbers(N):
    N=N*(N+1)//2
    return N
N=int(input())
result=sum_of_odd_numbers(N)
print(result)
#sum of N even numbers=N*(N+1)
#sum of N odd numbers=N**2 
#sum of N Natural numbers=N*(N+1)//2 if N>0
#sum of N whole numbers=N*(N+1)//2 if N>=0
