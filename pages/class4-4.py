# 全域變數與區域變數

length = 5  # 全域變數


def calculate_square_area():
    area = length * length  # 區域變數
    print("面積是", area)


calculate_square_area()

print("-" * 30)

length = 5  # 全域變數


def calculate_square_area2():
    area = length * length  # 區域變數
    print("面積是", area)


length = 10  # 全域變數
calculate_square_area2()

# print("-" * 30)

# length = 5  # 全域變數


# def calculate_square_are3():
#     area = length * length  # 區域變數


# length = 10  # 全域變數
# calculate_square_are3()
# print("面積是", area)

print("-" * 30)

length = 5  # 全域變數
area = 3.14 * 10**2  # 全域變數


def calculate_square_area4():
    area = length * length


calculate_square_area4()
print("面積是", area)

# print("-" * 30)

# length = 5  # 全域變數
# area = 3.14 * 10**2  # 全域變數


# def calculate_square_area5():
#     print("面積是", area)
#     area = length * length
#     print("面積是", area)


# calculate_square_area5()

print("-" * 30)

length = 5  # 全域變數
area = 3.14 * 10**2  # 全域變數


def calculate_square_area6():
    area = length * length
    return area


area = calculate_square_area6()
print("面積是", area)

print("-" * 30)

length = 5  # 全域變數
area = 3.14 * 10**2  # 全域變數


def calculate_square_area7():
    global area
    area = length * length


calculate_square_area7()
print("面積是", area)
