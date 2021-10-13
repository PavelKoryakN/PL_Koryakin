n = int(input("Введите N"))
num1 = 0
num2 = 1
for i in range(1, n):
    summa = num1+num2
    num1 = num2
    num2 = summa
    i = i+1
print(summa)