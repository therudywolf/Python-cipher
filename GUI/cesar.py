plainText = input("Шифруемый текст: ")
distance = int(input("Дистанция: "))
code = ""
decode = ""

alphavite = ',.!:\'\"#?@[](){} '
alphavite1 = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alphavite2 = 'АБВГДДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЪЫЬЭЮЯ'

for i in plainText:
    global code
    if i.islower():
        code += alphavite1[(alphavite1.find(i) + distance) % len(alphavite1)]
    elif i.isupper():
        code += alphavite2[(alphavite2.find(i) + distance) % len(alphavite2)]
    else:
        code += alphavite[(alphavite.find(i) + distance) % len(alphavite)]
print("Зашифровка:", code)

for i in code:
    if i.islower():
        decode += alphavite1[(alphavite1.find(i) - distance) % len(alphavite1)]
    elif i.isupper():
        decode += alphavite2[(alphavite2.find(i) - distance) % len(alphavite2)]
    else:
        decode += alphavite[(alphavite.find(i) - distance) % len(alphavite)]
print("Расшифровка:", decode)
