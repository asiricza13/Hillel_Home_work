'''
Вам потрібно обчислити середнє значення квадратів непарних чисел зі списку. Використовуйте функції map,
 filter та reduce.
 '''
import functools
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [i for i in numbers if i % 2 != 0]
sq_odd = map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numbers))
sum_sq_odd = functools.reduce(lambda x, y: x + y, sq_odd)
res = sum_sq_odd / len(odd_numbers)
print(res)