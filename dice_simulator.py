# 1. understand the proble,
# 2 think
# 3 write the algorithm
# 4 main logic and start working
# 5 modify the code

#1.dice 2.randm no 3.looping

# algorihtm
#1 dev random no 2 check the no 3 print and face 4 looping

import random

go = 'y'

while go == 'y':
    x = round(random.randint(1, 6))
    if x == 1:
        print("---------")
        print("|       |")
        print("|   o   |")
        print("|       |")
        print("---------")
    if x==2:
        print("---------")
        print("|       |")
        print("| o   o |")
        print("|       |")
        print("---------")
    if x==3:
        print("---------")
        print("| o    o|")
        print("|   o   |")
        print("|       |")
        print("---------")
    if x==4:
        print("---------")
        print("|o     o|")
        print("|      |")
        print("|o     o|")
        print("---------")
    if x==5:
        print("---------")
        print("|o     o|")
        print("|   o   |")
        print("|o     o|")
        print("---------")
    if x==6:
        print("---------")
        print("|o     o|")
        print("|o     o|")
        print("|o     o|")
        print("---------")
    go = input("input y run again or to quit n: ")
