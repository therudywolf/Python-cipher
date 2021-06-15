from math import gcd
import random

def ElGamal_realisation(msg):
    final_EL_otvet = ""
    final_EL_check = ""
    # инициализация алфавита
    alphavit = {'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4,
                'е': 5, 'ж': 6, 'з': 7, 'и': 8, 'й': 9,
                'к': 10, 'л': 11, 'м': 12, 'н': 13, 'о': 14,
                'п': 15, 'р': 16, 'с': 17, 'т': 18, 'у': 19,
                'ф': 20, 'х': 21, 'ц': 22, 'ч': 23, 'ш': 24,
                'щ': 25, 'ъ': 26, 'ы': 27, 'ь': 28, 'э': 29,
                'ю': 30, 'я': 31, ' ': 32, ",": 33, ".": 34,
                'А': 35, 'Б': 36, 'В': 37, "Г": 38, "Д": 39,
                'Е': 40, 'Ж': 41, 'З': 42, 'И': 43, 'Й': 44,
                'К': 45, 'Л': 46, 'М': 47, 'Н': 48, 'О': 49,
                'П': 50, 'Р': 51, 'С': 52, 'Т': 53, 'У': 54,
                'Ф': 55, 'Х': 56, 'Ц': 57, 'Ч': 58, 'Ш': 59,
                'Щ': 60, 'Ъ': 61, 'Ы': 62, 'Ь': 63, 'Э': 64,
                'Ю': 65, 'Я': 66, '!': 67, "?": 68, ";": 69}

    # проверка на простое число
    def IsPrime(n):
        d = 2
        while n % d != 0:
            d += 1
        return d == n

    # расширенный алгоритм Евклида или (e**-1) mod fe
    def modInverse(e, el):
        e = e % el
        for x in range(1, el):
            if ((e * x) % el == 1):
                return x
        return 1

    # выбор простого целого P, выбор целого числа G,G<P
    def is_prime(num, test_count):
        if num == 1:
            return False
        if test_count >= num:
            test_count = num - 1
        for x in range(test_count):
            val = random.randint(1, num - 1)
            if pow(val, num - 1, num) != 1:
                return False
        return True

    def gen_prime(n):
        found_prime = False
        while not found_prime:
            p = random.randint(2 ** (n - 1), 2 ** n)
            if is_prime(p, 1000):
                return p

    p = gen_prime(10)
    final_EL_otvet += "P =" + str(p) + '\n'
    #print()
    g = random.randint(2, p - 1)
    final_EL_otvet += "G =" + str(g) + '\n'
    #print()
    # отправитель выбирает случайное целое число X,1<x<(p-1)
    x = random.randint(2, p - 2)
    y = (g ** x) % p
    final_EL_otvet += "Открытый ключ(Y)={}\nСекретный ключ(X)={}".format(y, x) + '\n'
    #print()
    # хэшируем сообщение
    msg_list = list(msg)
    alpha_code_msg = list()
    for i in range(len(msg_list)):
        alpha_code_msg.append(int(alphavit.get(msg_list[i])))
    final_EL_otvet += "Длина исходного сообщения {} символов".format(len(alpha_code_msg)) + '\n'
    #print()

    def hash_value(p, alpha_code):
        i = 0
        hashing_value = 1
        while i < len(alpha_code_msg):
            hashing_value = (((hashing_value - 1) + int(alpha_code_msg[i])) ** 2) % p
            i += 1
        return hashing_value

    hash_code_msg = hash_value(p, alpha_code_msg)
    final_EL_otvet += "Хэш сообщения:= {}".format(hash_code_msg) + '\n'
    #print()
    # генерация случайное целое число K
    k = 1
    while True:
        k = random.randint(1, p - 2)
        if gcd(k, p - 1) == 1:
            final_EL_otvet += "K =" + str(k) + '\n'
            break

    # отправитель вычисляет число целое число а
    a = (g ** k) % p
    # вычисляем b
    b = modInverse(k, p - 1) * ((hash_code_msg - (x * a)) % (p - 1))
    # b = modInverse((int(hash_code_msg) - int(x)*int(a)),p-1)
    final_EL_otvet += "Значение подписи:S={},{}".format(a, b) + '\n'
    # print()

    # проверка подписи (передвём m, a,b)
    check_hash_value = hash_value(p, alpha_code_msg)
    a_1 = ((y ** a) * (a ** b)) % p
    final_EL_check += "A1={}".format(a_1) + '\n'
    # print()
    a_2 = (g ** check_hash_value) % p
    final_EL_check += "A2={}".format(a_2) + '\n'
    # print()
    if a_1 == a_2:
        final_EL_check += str(a_1) + " = " + str(a_2) + '\n'
        final_EL_check += "Подпись верна" + '\n'
    else:
        final_EL_check += str(a_1) + " != " + str(a_2) + '\n'
        final_EL_check += "Подпись неверна"
    return final_EL_otvet, final_EL_check
    
"""msg = input("Введите сообщение:")
otvet = ElGamal_realisation(msg)
print(otvet[0], '\n' + otvet[1])"""

