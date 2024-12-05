a=list(map(int,input().split()))
key=int(input())
left=0
right=len(a)-1
a.sort()
while left<=right:
    mid=left+(right-left)//2
    if a[mid]==key:
        print("key found")
        break
    elif a[mid]<key:
        left=mid+1
    elif a[mid]>key:
        right=mid-1
    else:
        print("key not found")

