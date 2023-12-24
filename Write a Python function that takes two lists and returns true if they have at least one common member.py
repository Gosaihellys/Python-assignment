list1=[1,2,3,4,5]
list2=[5,6,7,8,9]
result = False
for x in list1:
 for y in list2:
       if x==y:
           result = True
           print(result)
if result:
     print("List have at least one common member")
else:
    print("List do not have any commom member")
