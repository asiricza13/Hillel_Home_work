''' ДЗ 19. Реалізуйте генератор, який буде генерувати "решітку" заданого розміру N x N.'''

def grid(a: int, b: int):
    while b != 0:
        yield a * '#'
        b -= 1

funk = grid(a=3,b=3)
for num in funk:
    print(num)