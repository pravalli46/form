#finding the greatest element and swapping it to the last index
def selction_sort(n):
    L=len(n)
    for i in range(L):
        min_index=i
        for j in range(i+1,len(n)):
            if n[j]<n[min_index]:
                min_index=j
        n[i],n[min_index]=n[min_index],n[i]
    print(n)
a=list(map(int,input().split()))
selction_sort(a)