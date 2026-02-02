# 這是單行註解
"""
這是多行註解
"""

n1 = 13  # 這是整數
f1 = 3.14  # 這是浮點數
b1 = True  # 這是布林值
s1 = "hello"  # 這是字串

print(3)
print(3.14)
print(True)
print("hello")

a = 10
b = 20
print(a + b)  # 加法
print(a - b)  # 減法
print(a * b)  # 乘法
print(a / b)  # 除法
print(a // b)  # 整除
print(a % b)  # 取餘數
print(a**2)  # 次方

print("hello" + "world")  # 字串連接
print("hello" + " " + "world")  # 字串連接
print("hello" * 3)  # 字串重複
print("hello" + "word" * 3)  # 字串連接與重複

name = "Alice"
age = 25
new_str = f"My name is {name}, and I am {age} years old."  # f-string
print(new_str)

print(len(""))  # 0
print(len("hi"))  # 2
print(len("hello"))  # 5
print(type(10))
print(type(True))
print(type("hello"))

print(int(True))  # 1
print(int(False))  # 0
print(type("1234"))  # 1234

print(float("3.14"))  # 3.14
print(float(10))  # 10

print(bool(1))  # True
print(bool(0))  # False
print(bool(-2))  # True
print(bool(""))  # False
print(bool("hello"))  # True

print(str(1234))  # "1234"
print(str(3.14))  # "3.14"
print(str(True))  # "True"

# in1 = input("請輸入內容: ")  # 取得使用者輸入
# print("你輸入的內容是:", in1)
# print(type(in1))  # str

in2 = int(input("請輸入半徑: "))
area = 3.14 * "r" ** 2
print(f"半徑為{"r"}的圓面積為{area}")
