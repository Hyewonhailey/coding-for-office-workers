# 함수 functions
# 입력값 parameters, 반환값 return

def hello_friends(name):
    print("hello, {}".format(name))

name1 = "marco"
name2 = "jane"
name3 = "john"
name4 = "tom"

hello_friends(name1)
hello_friends(name2)
hello_friends(name3)
hello_friends(name4)

# 1. 입력값 있고 반환값 있음
def sum(a, b):
    return a + b

# 2. 입력값 있고 반환값 없음
def hello_friends(name):
    print("hello, {}".format(name))

# 3. 입력값 없고 반환값 있음
def return_1():
    return 1

# 4. 입력값 없고 반환값 없음
def hello_world():
    print("hello world")

# num_1 = return_1()
# print(num_1)
