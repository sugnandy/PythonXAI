import random


def roll_dice(times):
    results = []  # 用來裝所有骰子結果

    for i in range(times):
        dice = random.randint(1, 6)  # 丟一次骰子
        results.append(dice)  # 存起來

    return results


# 使用者輸入丟骰子次數
times = int(input("請輸入要丟骰子的次數："))

# 呼叫函數
dice_results = roll_dice(times)

# 顯示結果
print("骰子結果是：", dice_results)
