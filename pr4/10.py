n = int(input("Введите N"))
k = int(input("Введите K"))
num1 = 1
num2 = 1
m = 0
summa = 0
for i in range(3, n+k+1):
    if i<=k:
        m = num1+num2

    summa = num1+num2
    num1 = num2
    num2 = summa
print(summa-m)

