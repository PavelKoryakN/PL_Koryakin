n = int(input("Введите N"))
k = 0
fact = 1
summa = 0
while k+1 <= n:
    k = k+1
    fact = fact*k
    summa = summa+fact
print(summa)