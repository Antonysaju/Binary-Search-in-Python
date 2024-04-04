list1=[]
e= int(input("Please enter the total number of elements in the list: "))
for i in range(e):
    element= int(input("Please enter a number: "))
    list1.append(element)
print(list1)

list1.sort()
print(list1)

key= int(input("Please enter a number to search for: "))

low= 0
high= e-1
found= False

while found is not True:

    mid= (low+high)//2

    if key == list1[mid]:
        print(key, " found at location ", mid)
        found= True

    elif key > list1[mid]:
        low= mid+1

    elif key < list1[mid]:
        high= mid-1

    else:
        print("Key not found")
        

