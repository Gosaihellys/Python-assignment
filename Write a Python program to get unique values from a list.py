def unique(list1):
    unique_list=[]
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
        print(x)	
list1 = [10,20,10,30,40,40]
print("The unique value from 1st list ")
unique(list1)
list2 = [1,2,1,1,3,4,3,3,5]
print("The unique value from 2nd list ")
unique(list2)

