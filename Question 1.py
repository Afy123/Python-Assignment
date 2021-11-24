myList = []
length = int(input("Enter number of elements: "))
for i in range(0, length):
    val = int(input())
    myList.append(val)

temp = myList[-1]
myList[-1] = myList[0]
myList[0] = temp

print("List after Interchanged : ",myList )