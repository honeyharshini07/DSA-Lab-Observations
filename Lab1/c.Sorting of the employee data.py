def binary_search(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return -1

n=int(input("Enter the employee Ids:"))
arr=[]
print("Enter the elmemts in a sorted order:")
for i in range(n):
    arr.append(int(input()))
key=int(input("Enter the employee Id:"))
result=binary_search(arr,key)
if result!=-1:
    print("The employee Id is found")
else:
    print("The employee Id is not found")
