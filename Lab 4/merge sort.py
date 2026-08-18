def merge_sort(arr):
    #the base condition
    if len(arr)<=1:
        return arr
    #dividing the array
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    #recurssive calls
    merge_sort(left)
    merge_sort(right)
    i=0
    j=0
    k=0
    #merging the two sorted halves
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    #copy the remaining elements of left array
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    #copy the remaining elements of right array
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1
#enter the input
n=int(input("Enter the number of elements: "))
arr=[]
print("Enter the numbers:")
for i in range(n):
    arr.append(int(input()))
#function call
merge_sort(arr)
#printing the outputs
print("Merged array",arr)
