d = input("Дробь: ")
d = d.split("/")
try:
    p = (int(d[0])/int(d[1])) * 100
except ZeroDivisionError:
    d = input("Дробь: ")
    d = d.split("/")
except d[0]>d[1]:
    d = input("Дробь: ")
    d = d.split("/")
finally:
    p = (int(d[0])/int(d[1])) * 100
if p<=1:
    print("E")
elif p >=99:
    print("F")
else:
    print(str(round(p))+"%")