import random

target = random.randint(1, 100)

min_val = 0
max_val = 100
while True:
    num = int(input(f"請輸入{min_val}-{max_val}之間的數字: "))
    if num < min_val or num > max_val:
        print("非法輸入範圍")
    elif num < target:
        print("再大一點")
        min_val = num + 1
    elif num > target:
        print("再小一點")
        max_val = num - 1
    else:
        print("猜對了")
        break
