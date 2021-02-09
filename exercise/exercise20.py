a=[1,2,3,4,5,6,7,8,9,10]
print(len(a))
def is_in_list(a,nr):
    if nr in a:
        return True
    else:
        return False



nr=int(input("Enter the number:"))
if is_in_list(a,nr):
    print("Number:",nr,"is in the list")
else:
    print("Number:", nr, "isnt in the list")