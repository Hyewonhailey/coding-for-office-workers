# 구구단 프로그램

# print("몇 단을 출력 하시겠습니까?")
#     input = "x"
#     y = list(1, 2, 3, 4, 5, 6, 7, 8, 9)
#         if input = "x"
#             while ("x" * "y")
#                 print ("x" * "y")

dan = int(input("몇 단을 출력 하시겠습니까?"))
for num in range(1, 10):
    print("{} * {} = {}".format(dan, num, dan * num))
