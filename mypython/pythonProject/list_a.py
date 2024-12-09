numlist=[8,7,6,5,4,3,2,1]
print(numlist)


print(numlist[0])
print(numlist[-1])
print(numlist[1])

numlist[0]=1
print(numlist)

numlist.append(9)
print(numlist)

numlist.insert(4,5)
print(numlist)

#删除指定的值，只删除第一个
numlist.remove(7)
print(numlist)

numlist.sort()
print(numlist)
