alphavite = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'  # алфавит
alphavite2 = alphavite.upper()
alphavite3 = ',.!:\'\"#?@[](){} '


text = input('Введите сообщение \n')  # Ввод сообщения
code = ''  # Зашифрованное сообщение
krya = 0
for i in text:  # блок шифрования
    if i.islower():
        code += alphavite[(alphavite.find(i) + krya) % len(alphavite)]
    elif i.isupper():
        code += alphavite2[(alphavite2.find(i) + krya) % len(alphavite2)]
    else:
        code += alphavite3[(alphavite3.find(i) + krya) % len(alphavite3)]
    krya += 1
print(code)  # вывод зашифровнного текста

decode = ''
krya = 0

for i in code:
    if i.islower():
        decode += alphavite[(alphavite.find(i) - krya) % len(alphavite)]
    elif i.isupper():
        decode += alphavite2[(alphavite2.find(i) - krya) % len(alphavite2)]
    else:
        decode += alphavite3[(alphavite3.find(i) - krya) % len(alphavite3)]
    krya += 1

print(decode)
