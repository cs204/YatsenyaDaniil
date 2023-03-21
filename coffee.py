k = 50
while k > 0:
    print("Нужная сумма:",k)
    coin = int(input("Вставьте монету: "))
    if (coin == 50) or (coin == 20) or (coin == 10) or (coin == 5):
        k = k - coin
print("Ваша сдача:", abs(k))