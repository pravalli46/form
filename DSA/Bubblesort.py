def bubble_sort(n):
    L=len(n)
    for i in range(L):
        for j in range(0,L-i-1):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
    print(n)
a=list(map(int,input().split()))
bubble_sort(a)