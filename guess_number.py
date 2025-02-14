import time
import random

# guess number ( 1 - 100 )

ans = random.randint(1, 100)
quit = False
while not quit:
    a = int(input("please input your num(from 1 to 100):"))

    if a == ans:
        print("good job!!")
        while 1 :
            t = input("do you want to continue ? (y / n)\n")
            if t == 'y' or t == '1' :
                ans = random.randint(1, 100)
                break
            elif t == 'n' or t == '0' :
                quit = True
                break


    elif a > ans :
        print("your num id bigger!")
    else :
        print("your num is smaller!")

