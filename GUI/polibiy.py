alphavite = 'абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ, .!\"\'#?@[](){}'  # алфавит

print('Алгоритм шифрования Полибий')

text = input('Введите сообщение \n')  # .lower() #Ввод сообщения
encode = ''  # Зашифрованное сообщение

for i in text:  # блок шифрования
    encode += str(alphavite.find(i) // 8 + 1) + \
        str(alphavite.find(i) % 8 + 1) + ' '
    # определяем 2 числа, номер строки, как целое от деления позиции символа
    # в алфавите на 8, и номер столбца, как остаток от деления позиции символа на 8
print(encode)  # вывод зашифровнного текста

text = encode.split()
decode = ''

for i in text:
    decode += alphavite[(int(i[0]) - 1) * 8 + int(i[1]) - 1]


print(decode)
