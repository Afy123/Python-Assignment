myList = []
length = int(input("Enter number of elements: "))
for i in range(0, length):
    val = int(input())
    myList.append(val)

smallest = min(myList)
print("Smallest number in the list is : ",smallest)