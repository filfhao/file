print("Hello!")
from random import *
b = randint(1,100)
a = int(input("vidp"))
c = 1
while a != b:
    if a > b:
        print("Вибери менше число")
    if a < b:
        print("Вибери більше число")
    c = c + 1
    a = int(input("vidp"))
if a == b:
        print("Правильно, це",b)
        print("Кількість спроб:",c)