print(1 == 1)  # True
print(1 != 1)  # False
print(3 > 2)  # True
print(2 < 1)  # False
print(3 >= 3)  # True
print(2 <= 1)  # False

print(not True)  # False
print(not False)  # True

print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False or False)  # False

print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

password = input("請輸入密碼: ")

if password == "1234":
    print("登入成功")

if password == "1234":
    print("登入成功")
else:
    print("密碼錯誤")

if password == "1234":
    print("登入成功")
elif password == "5678":
    print("登入成功")
else:
    print("密碼錯誤")
