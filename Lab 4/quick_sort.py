def quick_sort(a, low, high):
    #the base condition
    if low < high:
        i = low
        j = high
        pivot = low
        while i < j:
            #element greater than or equal to the pivot
            while i <= high and a[i] <= a[pivot]:
                i += 1
            #element smaller than the pivot
            while a[j] > a[pivot]:
                j -= 1
            if i < j:
                a[i], a[j] = a[j], a[i]
        #placing the pivots in the positions
        a[pivot], a[j] = a[j], a[pivot]
        #recurrively sortng the left and right parts
        quick_sort(a, low, j - 1)
        quick_sort(a, j + 1, high)
#enter the inputs
a = list(map(int, input("Enter numbers to sort: ").split()))
n = len(a)
#function call
quick_sort(a, 0, n - 1)
#printing the output
print("Sorted array:")
print(a)

