'''
Напишіть програму, яка підраховує і роздруковує кількість появ кожного символу у введеному рядку.

Вхідні дані:

abcabcdfghj
'''


string = "abcabcdfghj"

dict = {}
for i in string:
    dict[i] = string.count(i)
print(dict)

