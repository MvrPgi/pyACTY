# list - is a collection which is ordered and changeable. Allows duplicate members.

#thislist =["apple","banana","cherry","orange","kiwi","melon","mango"]
#thislist[1:3] = ["strawberry","raspberry"]
#print(thislist)
#________________________________________________________________________________
#thislist =["apple","banana","cherry","orange","kiwi","melon","mango"]
#thislist.insert(2,"raspberry")
#print(thislist)
#________________________________________________________________________________
#tropical =["orange","kiwi","melon","mango"]
#________________________________________________________________________________
#//INSERT
#thislist =["apple","banana","cherry","orange","kiwi","melon",#"mango"]
#thislist.append("raspberry")
#print(thislist)
#________________________________________________________________________________
#//EXTEND
#thislist =["orange","kiwi","melon","mango"]
#tropical =["raspberry"]
#thislist.extend(tropical)
#print(thislist)
#________________________________________________________________________________
#//DELETE
#thislist =["orange","kiwi","melon","mango"]
#tropical =["raspberry"]
#del thislist[0]
#del thislist[0_3]
#thislist.remove("mango")
#print(thislist)
#________________________________________________________________________________
#//POP
#thislist =["orange","kiwi","melon","mango"]
#tropical =["raspberry"]
#thislist.pop(3)
#print(thislist)
#________________________________________________________________________________
#//CLEAR
#thislist =["orange","kiwi","melon","mango"]
#tropical =["raspberry"]
#print(thislist)
#thislist.clear()
#print(thislist)
#________________________________________________________________________________
#thislist =["orange","kiwi","melon","mango"]
#tropical =["raspberry"]
#thislist.append(tropical)
#for x in thislist:
#[rint(x, end= ' ')
#________________________________________________________________________________
## LOOP APPEND
#thislist =["apple","banana","cherry"]
#tropical =["orange","kiwi","melon","mango"]
#newlist = []
#for x in tropical:
    #if "a" in x:
      #newlist.append(x)

#print(newlist)
#________________________________________________________________________________
#SORTING
#thislist =["apple","banana","cherry"]
#tropical =["orange","kiwi","melon","mango"]
#tropical.sort()
#print(tropical)

#list1 = ["a","b","c"]
#list2 = [1,2,3]

#for x,y in zip(list2,list1):
    #print(str(x)+y, end=" ")

#print(list1)
#________________________________________________________________________________
#list1 = ["a","b","c"]
#list2 = [1,2,3]
#list2.remove(4)
#rint(list2)
#for i in enumerate(list1):
    #list1.insert(2*i ,i)
#print(list1)
#________________________________________________________________________________