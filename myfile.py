import math
import time
import sys
print("Hello, this is test my docker container for linux centos")
time.sleep(0.5)
a = float(input("Please write a parametr: "))
b = float(input("Please write a parametr: "))
c = float(input("Please write a parametr: "))
answer = int(0)
def choise():
        global answer #рефакторинг 1 ГЛОБАЛ ПЕРЕМЕННАЯ
        choise = str(input("Please, write you wont operation: "))
        if choise == "+":
            answer = a + b
        elif choise == "-":
            answer = a - b
        elif choise == "*":
            answer = a ** b
        elif choise == "/":
            answer = a / b
        else:
            print("Try again! Example: '+ , -, *, /' ")
            time.sleep(2)
            sys.exit()

choise()
print("You result is: ", answer)
