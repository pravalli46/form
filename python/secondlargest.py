l=list(map(int,input().split()))
first_largest=l[0]
second_largest=l[0]
for i in l:
    if i>=first_largest:
        second_largest=first_largest
        first_largest=i
print(second_largest)
print(first_largest)