def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1
n=int(input("Enter the number of elements:"))
arr=[]
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))
key=int(input("Enter the elements to search:"))
result=linear_search(arr,key)
if result!=-1:
    print("Element is found at the index:",result)
else:
    print("Elemnet is not found at the index")
