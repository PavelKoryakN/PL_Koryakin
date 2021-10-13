a = int(input("Введите А"))
b = int(input("Введите B"))
a = a+1
while a > b:
    a = a-1
    if a % 2 == 1:
        print(a, end=";")

