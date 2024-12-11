list1=[1,"hello",55.5]
print(list1)
print(list1[1])
list1[1]="world"
list1[0]=90.90
print(list1)
list2=[list1,234,00]
print(list2[0])
print(list2)
list3=[('t','b'),90,"luck"]
print(list3)
t=list3[0]
print(t)
list4=[list1,'a','a']
print(list4)
list4.extend(list3)
print(list4)
print(list4.index(list1))#list indexing of nested list
print(list4[2:5])#list slicing
list5=list1 + list2
print(list5)#list concatenation
print(list5[::-1])#list reverse
print(5*list5)#list repetition
print('a' in list5)#membership
list1.append("hello")#append
print(list1)
list6=[1,2,3,2,4,5,7,6]
list6.remove(2)
print(list6)#remove
print(list6.pop())#poping
print(list6)
list6.clear()
print(list6)
list7=[1,2,2,2,2,3,4,6,7,8]
print(list7.count(90))
print(list7.count(2))
list7.sort()
print(list7)
#list1.sort()
#print(list1)
list7.reverse()
print(list7)
list7.sort(reverse=True)#descending order
print(list7)