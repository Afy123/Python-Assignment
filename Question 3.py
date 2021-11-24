myList = []
length = int(input("Enter the element : "))
for i in range(0,length):
    val = int(input())
    myList.append(val)

for num in myList:
   if num % 2 == 0:
      print(num , end = " ")