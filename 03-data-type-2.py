# 목록 list, tuple
# 사전 dict - dictionary
# 집합 set

# list []
print("list")
list_a = [1, 2, 3]
print(list_a)
print(type([1 ,2, 3]))
# # indext는 0부터 시작합니다.
print(list_a[0])
print(list_a[1])
print(list_a[2])
# # slice
print(list_a[0:2])
list_a.append(4)
print(list_a)
#
list_a.remove(2)
print(list_a)
#
list_a.clear()
print(list_a)


# tuple (1, )
print("tuple")
tuple_a = (1, 2, 3)
print(tuple_a)
print(type(tuple_a))
# tuple_a.append(4)
