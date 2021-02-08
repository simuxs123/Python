a=[5,4,2,1,2,3,4,5,6,5,4,3,2,1]
def new_list_set(arr):
    return list(set(arr))
def new_list(arr):
    c = []
    for i in range(len(arr)):
        if arr[i] not in c:
            c.append(arr[i])
    return c


print(new_list(a))
print(new_list_set(a))