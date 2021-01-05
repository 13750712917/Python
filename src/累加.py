from time import sleep
import os

# a = os.system("adb shell pm list packages -3")
# print(type(a))
# print(a)

a = 1000 # 全局变量
a1 = 10
a2 = 20

def cha(x1 = 100,x2 = 99):
    b=10000 # 局部变量
    chazhi=a-x1-x2
    return chazhi
print(cha(a1,a2))