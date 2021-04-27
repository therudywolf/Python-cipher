import random


def a5_realisation(s):
    alph = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя.,-?!: "

    while len(s) % 8 != 0:
        randd = random.randint(0, 65)  # rand() % 65
        s2 = alph[randd]
        s = s + s2

    dva = [0] * 4500

    for i in range(0, len(s)):
        # 128 | | 64 | | 32 | | 16 | | 8 | | 4 | | 2 | | 1
        pos = alph.find(s[i])
        if pos >= 128:
            dva[i * 8 + 0] = 1
            pos = pos - 128
        if pos >= 64:
            dva[i * 8 + 1] = 1
            pos = pos - 64
        if pos >= 32:
            dva[i * 8 + 2] = 1
            pos = pos - 32
        if pos >= 16:
            dva[i * 8 + 3] = 1
            pos = pos - 16
        if pos >= 8:
            dva[i * 8 + 4] = 1
            pos = pos - 8
        if pos >= 4:
            dva[i * 8 + 5] = 1
            pos = pos - 4
        if pos >= 2:
            dva[i * 8 + 6] = 1
            pos = pos - 2
        if pos == 1:
            dva[i * 8 + 7] = 1

    krya = ""

    # Перевод сообщения в двоичный код
    for i in range(0, len(s) * 8):
        krya += str(dva[i])

    x2_code_text = "Двочный код сообщения: " + krya

    print_key = ""
    sh = [0] * 4500
    gamma = [0] * 64

    # Генерируем ключ
    for i in range(0, 64):
        randd = random.randint(0, 1)
        gamma[i] = randd
        print_key += str(gamma[i])
    gen_key = "Сгенерированный ключ:" + print_key

    for i in range(0, 4500):
        sh[i] = 0

    # Выработка гаммы
    for j in range(0, 4500):
        F = gamma[8] and gamma[29] or gamma[8] and gamma[51] or gamma[29] and gamma[51]
        if F == gamma[8]:
            zam = gamma[18] ^ gamma[17] ^ gamma[16] ^ gamma[13]
            gamma[18] = gamma[17]
            gamma[17] = gamma[16]
            gamma[16] = gamma[15]
            gamma[15] = gamma[14]
            gamma[14] = gamma[13]
            gamma[13] = gamma[12]
            gamma[12] = gamma[11]
            gamma[11] = gamma[10]
            gamma[10] = gamma[9]
            gamma[9] = gamma[8]
            gamma[8] = gamma[7]
            gamma[7] = gamma[6]
            gamma[6] = gamma[5]
            gamma[5] = gamma[4]
            gamma[4] = gamma[3]
            gamma[3] = gamma[2]
            gamma[2] = gamma[1]
            gamma[1] = gamma[0]
            gamma[0] = zam
        if F == gamma[29]:
            zam = gamma[40] ^ gamma[39]
            gamma[40] = gamma[39]
            gamma[39] = gamma[38]
            gamma[38] = gamma[37]
            gamma[37] = gamma[36]
            gamma[36] = gamma[35]
            gamma[35] = gamma[34]
            gamma[34] = gamma[33]
            gamma[33] = gamma[32]
            gamma[32] = gamma[31]
            gamma[31] = gamma[30]
            gamma[30] = gamma[29]
            gamma[29] = gamma[28]
            gamma[28] = gamma[27]
            gamma[27] = gamma[26]
            gamma[26] = gamma[25]
            gamma[25] = gamma[24]
            gamma[24] = gamma[23]
            gamma[23] = gamma[22]
            gamma[22] = gamma[21]
            gamma[21] = gamma[20]
            gamma[20] = gamma[19]
            gamma[19] = zam
        if F == gamma[51]:
            zam = gamma[63] ^ gamma[62] ^ gamma[61] ^ gamma[48]
            gamma[63] = gamma[62]
            gamma[62] = gamma[61]
            gamma[61] = gamma[60]
            gamma[60] = gamma[59]
            gamma[59] = gamma[58]
            gamma[58] = gamma[57]
            gamma[57] = gamma[56]
            gamma[56] = gamma[55]
            gamma[55] = gamma[54]
            gamma[54] = gamma[53]
            gamma[53] = gamma[52]
            gamma[52] = gamma[51]
            gamma[51] = gamma[50]
            gamma[50] = gamma[49]
            gamma[49] = gamma[48]
            gamma[48] = gamma[47]
            gamma[47] = gamma[46]
            gamma[46] = gamma[45]
            gamma[45] = gamma[44]
            gamma[44] = gamma[43]
            gamma[43] = gamma[42]
            gamma[42] = gamma[41]
            gamma[41] = zam
        # нахождение выходного бита
        sh[j] = gamma[18] ^ gamma[40] ^ gamma[63]

    print_gamma = ""
    for i in range(0, len(s) * 8):
        print_gamma += str(sh[i])

    gen_gamma = "Выработанная гамма:" + print_gamma

    # Шифруем текст в двоичном коде
    encrypt_dv_code = ""

    for i in range(0, int(len(s) / 8)):
        for j in range(0, 64):
            dva[j + i * 64] = dva[j + i * 64] ^ sh[j]
            encrypt_dv_code += str(dva[j + i * 64])

    shifr_text_x2 = "Зашифрованный текст (в двоичном виде):" + encrypt_dv_code

    # Расишфровываем текст в двоичном коде
    decrypt_dv_code = ""

    for i in range(0, int(len(s) / 8)):
        for j in range(0, 64):
            dva[j + i * 64] = dva[j + i * 64] ^ sh[j]
            decrypt_dv_code += str(dva[j + i * 64])

    deshifr_text_x2 = "Расшифрованный текст (в двоичном виде):" + \
        decrypt_dv_code

    # Переводи расшифрованный двоичный код в текст
    decrypt = ""
    for i in range(0, len(s)):
        # 128 | | 64 | | 32 | | 16 | | 8 | | 4 | | 2 | | 1
        pos = 0
        if dva[i * 8 + 0] == 1:
            pos = pos + 128
        if dva[i * 8 + 1] == 1:
            pos = pos + 64
        if dva[i * 8 + 2] == 1:
            pos = pos + 32
        if dva[i * 8 + 3] == 1:
            pos = pos + 16
        if dva[i * 8 + 4] == 1:
            pos = pos + 8
        if dva[i * 8 + 5] == 1:
            pos = pos + 4
        if dva[i * 8 + 6] == 1:
            pos = pos + 2
        if dva[i * 8 + 7] == 1:
            pos = pos + 1

        decrypt += str(alph[int(pos)])
    a5_decrypt = "Расшифрованный текст: " + decrypt

    return x2_code_text, gen_key, gen_gamma, shifr_text_x2, deshifr_text_x2, a5_decrypt


s = input("Введите сообщение:\n")  # ввод сообщения
otvet = a5_realisation(s)
print(otvet[0])
print(otvet[1])
print(otvet[2])
print(otvet[3])
print(otvet[4])
print(otvet[5])
