import random


def notepad_shenona(msg):
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

    def get_key(d, value):
        for k, v in d.items():
            if v == value:
                return k

    message = list(msg)
    message_len = len(message)
    msg_code_bin_list = list()
    for i in range(len(message)):
        msg_code_bin_list.append(alphavit.get(message[i]))
    open_text = "Текст:\n{}".format(msg_code_bin_list)
    key_list = list()
    for i in range(message_len):
        key_list.append(random.randint(0, 69))

    kluchick = "Ключ:\n{}".format(key_list)

    cipher_list = list()

    # Шифрование по с = m xor k
    for i in range(message_len):
        m = int(msg_code_bin_list[i])
        k = int(key_list[i])
        cipher_list.append(int(bin(m ^ k), base=2))
    shifr = "Шифр:\n{}".format(cipher_list)

    # Расшифрование по m = c xor k
    decipher_list = list()
    for i in range(message_len):
        c = int(cipher_list[i])
        k = int(key_list[i])
        decipher_list.append(int(bin(c ^ k), base=2))

    deciphered_str = ""
    for i in range(len(decipher_list)):
        deciphered_str += get_key(alphavit, decipher_list[i])
    deshifr_code = "Расшифрованный код:\n{}".format(decipher_list)
    deshifr_text = "Расшифрованный текст:\n{}".format(deciphered_str)

    return open_text, kluchick, shifr, deshifr_code, deshifr_text


"""
msg = input("Введите текст: \n")
otvet = notepad_shenona(msg)
print(otvet[0])
print(otvet[1])
print(otvet[2])
print(otvet[3])
print(otvet[4])
"""
