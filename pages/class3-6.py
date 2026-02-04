D1 = {}
D2 = {"A": 90, "B": 80, "C": 70, "D": 60}
print(D1)
print(D2)
print(D2["A"])  # 90
print(D2["C"])  # 70

print("-" * 30)

D3 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

for key in D3:
    print(key)

print(D3.keys())  # dict_keys(['a', 'b', 'c', 'd', 'e'])
for key in D3.keys():
    print(key)

print(D3.values())  # dict_values([1, 2, 3, 4, 5])
for value in D3.values():
    print(value)

print(D3.items())  # dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
for key, value in D3.items():
    print(f"{key}: {value}")

D3 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
D3["f"] = 6  # 新增"f":6
print(D3)
D3["a"] = 10  # 更新"a":10
print(D3)

print("-" * 30)

D3 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
D3.pop("c")  # 刪除 key為"c"的項目
print(D3)
popValue = D3.pop("f", "Error: key not found")  # 若不存在則回傳預設值
print(popValue)
print(D3)

print("-" * 30)

print(len({}))  # 0
print(len({"apple": "蘋果"}))  # 1
print(len({"a": 1, "b": 2, "c": 3}))  # 3

print("-" * 30)
D3 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print("d" in D3)  # True
print("f" in D3)  # False
print(2 in D3)  # False

print("-" * 30)

L1 = [1, 2, 3, 4, 5]
print(4 in L1)  # True
print(6 in L1)  # False

print("-" * 30)

import random

scores = {"國文": [], "英文": [], "數學": [], "自然": [], "社會": []}
for key in scores:
    for i in range(10):
        scores[key].append(random.randint(60, 100))

print("計算各科平均成績:")
for key in scores:
    totel = 0
    for score in scores[key]:
        totel += score
    average = totel / 10
    print(f"{key} 平均成績: {average}")
