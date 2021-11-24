firstList = ["APPLE","ORANGE","BANANA"]
secondList = ["PINAPPLE","GRAPE","APPLE"]
length = len(firstList)

print(length)


firstList = ["APPLE","ORANGE","BANANA"]
secondList = ["PINAPPLE","GRAPE","APPLE"]
firstList.append(secondList)

print(firstList)

firstList = ["APPLE","ORANGE","BANANA"]
secondList = ["PINAPPLE","GRAPE","APPLE"]
firstList.extend(secondList)

print(firstList)

firstList = ["APPLE","ORANGE","BANANA"]
secondList = ["PINAPPLE","GRAPE","APPLE"]


for i in firstList:
    if i in secondList:
        print(i,"Is in it")


if i not in secondList:
        print(i,"Is not in it")
