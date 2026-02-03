L1 = []
print(L1)  # 空串列

L2 = [1, 2, 3, 4, 5]
print(L2)  # 純數字串列

L3 = ["apple", "banana", "cherry"]
print(L3)  # 純字串串列

L4 = ["apple", True, 3, 14]
print(L4)  # 混和型串列

L5 = [1, 2, 3, [4, 5]]
print(L5)  # 巢狀形串列

# 取用串列中的元素
print(L5[1])  # 2
print(L5[3])  # [4,5]
print(L5[3][0])  # 4

L6 = [1, 2, 3, "a", "b", "c"]
L7 = L6[::2]
print(L7)  # [1,3,"b"]
L8 = L6[1:4]
print(L8)  # [2,3,"a"]
L9 = L6[1:4:2]
print(L9)  # [2,"a"]
