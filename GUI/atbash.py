alphavite = ',.!:\'\"#?@[](){} '
text = input("Введите открытый текст: ")
code = ''  # Зашифрованное сообщение
for i in text:  # блок шифрования
    if i.isupper():
        # находим позицию символа в алфавите (начиная с 0)
        k = ord(i) % ord('А')
        # выбираем из алфавита символ, который меньше на k+1 чем длина алфавита
        code += chr(ord('Я') - k)
    elif i.islower():
        k = ord(i) % ord('а')
        code += chr(ord('я') - k)
    else:
        code += alphavite[len(alphavite) - alphavite.find(i) - 1]
print("Зашифровка:", code)  # Выводим зашифрованное сообщение

text_decode = code
if code == '':
    text_decode = text
global decode
decode = ''
for i in text_decode:  # блок расшифрования
    if i.isupper():
        # находим позицию символа в алфавите (начиная с 0)
        k = ord(i) % ord('А')
        # выбираем из алфавита сивол, который меньше на k+1 чем длина алфавита
        decode += chr(ord('Я') - k)
    elif i.islower():
        k = ord(i) % ord('а')
        decode += chr(ord('я') - k)
    else:
        decode += alphavite[len(alphavite) - alphavite.find(i) - 1]
print("Расшифровка:", decode)
