def search(ids, key, index):
    if index == len(ids):
        return -1

    if ids[index] == key:
        return index

    return search(ids, key, index + 1)

ids = [101, 205, 310, 415, 520]
key = int(input("Enter employee ID to search: "))
result = search(ids, key, 0)
if result != -1:
    print("Employee ID found at position:", result)
else:
    print("Value is not found")
