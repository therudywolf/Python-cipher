import random

# Вычисление простых чисел #
array = []
flag = False
for s in range(50, 1000):
    for i in range(2, s):
        if s % i == 0:
            flag = True
            break
    if flag == False:
        array.append(s)
    flag = False
#array.append("...")
print("Простые числа (s):", array, '\n')

# Простые числа
p = int(random.choice(array))
q = int(random.choice(array))
print("p = %d; q = %d" % (p, q))

n = p * q           # Произведение
Fn = (p-1)*(q-1)    # Функция Эйлера

print("n = %d; f(n) = %d\n" % (n, Fn))

# Подбор открытой экспоненты #
array2 = []
for meow in range(2, 10000):
    d = int((1 + 2 * Fn) / meow)
    if d * meow == 1 + 2 * Fn:
        array2.append(meow)

if array2 == []:
    print("Невозможно найти взаимно простое число D!")
    raise SystemExit

#array2.append("...")
print("Подходящие для открытой экспоненты числа(D): ", array2)

# Открытая экспонента
D = int(random.choice(array2))# Простое нечётное число не имеющее общих делителей с f(n)

print("Открытая экспонента (D) =", D, '\n')

"""
# Подбор натурального числа k #
array3 = []
for k in range(1, 1000):
    heh = int((1 + k * Fn) / D)
    if heh * D == 1 + k * Fn:
        array3.append(k)
#array3.append("...")
# print("k:", array3)
"""
k = 2

# Секретная экспонента
E = int((1 + k * Fn) / D)

print("Секретная экспонента(E) =", E)


# Условие на вычисление секретной экспоненты
if E * D != 1 + k * Fn:
    raise SystemExit

public_key = [D, n]      # Публичный ключ
private_key = [E, n]     # Приватный ключ

print("Публичный ключ: ", public_key)
print("Приватный ключ: ", private_key, '\n')

alphavit = {'а':0, 'б':1, 'в':2, 'г':3, 'д':4,
            'е':5, 'ж':6, 'з':7, 'и':8, 'й':9,
            'к':10, 'л':11, 'м':12, 'н':13, 'о':14,
            'п':15, 'р':16, 'с':17, 'т':18, 'у':19,
            'ф':20, 'х':21, 'ц':22, 'ч':23, 'ш':24,
            'щ':25, 'ъ':26, 'ы':27, 'ь':28, 'э':29,
            'ю':30, 'я':31, ' ':32, ",":33, ".":34,
            'А':35, 'Б':36, 'В':37, "Г":38, "Д":39,
            'Е':40, 'Ж':41, 'З':42, 'И':43, 'Й':44,
            'К':45, 'Л':46, 'М':47, 'Н':48, 'О':49,
            'П':50, 'Р':51, 'С':52, 'Т':53, 'У':54,
            'Ф':55, 'Х':56, 'Ц':57, 'Ч':58, 'Ш':59,
            'Щ':60, 'Ъ':61, 'Ы':62, 'Ь':63, 'Э':64,
            'Ю':65, 'Я':66, '!':67, "?":68, ";":69}

# Сообщение
"""
m = 0
message = input("Введите сообщение: ")

for krya in message:
    m += int(alf.find(krya))
print("Сообщение (m): ", m)
"""
#хэшируем сообщение
msg = input("Введите сообщение: ")
msg_list = list(msg)
alpha_code_msg = list()
for i in range(len(msg_list)):
    alpha_code_msg.append(int(alphavit.get(msg_list[i])))
print("Длина исходного сообщения {} символов".format(len(alpha_code_msg)))
print()

def hash_value(n,alpha_code):
    i = 0
    hashing_value = 1
    while i < len(alpha_code_msg):
        hashing_value = (((hashing_value-1) + int(alpha_code_msg[i]))**2) % n
        i += 1
    return hashing_value

hash_code_msg = hash_value(p, alpha_code_msg)
print("Хэш сообщения (m):= {}".format(hash_code_msg))

m = hash_code_msg

# Шифрование
Cm = (m ** D) % n
print("Цифровая подпись (Cm): ", Cm)

# Расшифрование
Dm = (Cm ** E) % n
print("Проверка цифровой подписи (Dm): ", Dm)

if m == Dm:
    print("Подпись верна!")
else:
    print("Подпись не верна!")