'''
Користувач вводить рядок,

Ваша задача — сформатувати строку в хештег.

Декілька правил:

жодних інших символів із набору string.punctuation бути не повинно, в тому числі і пробілів
довжини хештега повинен бути не більше 140 символів,
якщо довжина хештега більше 140 символів - обрізати підсумковий рядок до 140 символів.
Кожне слово починається з великої літери.
перед хештегом додати знак "#"
'''

text = input("Введіть рядок:")
txt1 = ' '.join(word.capitalize() for word in text.split())
txt2 = txt1.replace('!', '').replace('?', '').replace(',', '').replace('?','').replace('.','').replace(' ','')
txt3 = '#' + txt2[0:]
result = txt3[:140]
print(result)






