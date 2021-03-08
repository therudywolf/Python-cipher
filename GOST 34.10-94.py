import random
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


def hash_value(n, alpha_code):
    i = 0
    hash = 1
    while i < len(alpha_code):
        hash = (((hash-1) + int(alpha_code[i]))**2) % n
        i += 1
    return hash

# p = int(input("Введите простое число p: "))
# q = int(input("Введите простое число q: "))
p = int(random.choice(array))
print("p = ", p)
q = int(random.choice(array))
print("q = ", q)
a = 1

while True:
    a = random.randint(1, p-1)
    if a**q % p == 1:
        print("a =", a)
        break


array2 = []
flag2 = False
for s in range(2, q):
    for i in range(2, s):
        if s % i == 0:
            flag2 = True
            break
    if flag2 == False:
        array2.append(s)
    flag2 = False

x = int(random.choice(array2))
print("x = ", x)
# x = int(input("Введите простое число x, x < q: "))
y = a**x % p
k = int(random.choice(array2))
print("k = ", k)
# k = int(input("Введите простое число k, k < q: "))
r = (a**k % p) % q

#хэшируем сообщение
msg = input("Введите сообщение: ")    # .lower()
msg_list = list(msg)
alpha_code_msg = list()
for i in range(len(msg_list)):
    alpha_code_msg.append(int(alphavit.get(msg_list[i])))
print("Длина исходного сообщения {} символов".format(len(alpha_code_msg)))
hash_code_msg = hash_value(p, alpha_code_msg)
print("Хэш сообщения:= {}".format(hash_code_msg))
#print()

s = (x*r+k*hash_code_msg) % q

print("Цифровая подпись = ", r % (2**256), ",", s % (2**256))

#  Проверка цифровой подписи
v = (hash_code_msg**(q-2)) % q
z1 = s*v % q
z2 = ((q-r)*v) % q
u = (((a**z1)*(y**z2)) % p) % q
print(r, " = ", u)
if u == r:
    print("r = u, следовательно:")
    print("Подпись верна")
else:
    print("Подпись неверна")
