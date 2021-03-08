import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
from reshetka_kardano_final import reshetka_kardano    # функция алгоритма шифрования решётки кардано
from re import findall    # метод из модуля для разбиения строки на подстроки
from vernam import notepad_shenona
from A5_first import a5_realisation
from A5_second import a52_realisation
from AES import AES_realize
from Magma import prZamena, Gamma, GammaOBR, imitovstavka
from RSA import RSA_realisation
from ElGamal import ElGamal_realisation
from GOST_34_10_94 import GOST_34_10_94_realisation
from GOST_34_10_2012 import GOST_34_10_2012_realisation

# Функция выбора алгоритма шифрования/////////////////////////////////////////////////////////////////////////////////
def select():
    global krya
    if combotext.get() == "Атбаш":
        krya = 1
    elif combotext.get() == "Цезарь":
        krya = 2
    elif combotext.get() == "Полибий":
        krya = 3
    elif combotext.get() == "Тритемий":
        krya = 4
    elif combotext.get() == "Белазо":
        krya = 5
    elif combotext.get() == "Виженер":
        krya = 6
    elif combotext.get() == "Матричный":
        krya = 7
    elif combotext.get() == "Плейфер":
        krya = 8
    elif combotext.get() == "Вертикальная перестановка":
        krya = 9
    elif combotext.get() == "Решётка Кардано":
        krya = 10
    elif combotext.get() == "Одноразовый блокнот Шеннона":
        krya = 11
    elif combotext.get() == "A5/1":
        krya = 12
    elif combotext.get() == "A5/2":
        krya = 13
    elif combotext.get() == "AES":
        krya = 14
    elif combotext.get() == "Магма (Простая замена)":
        krya = 15
    elif combotext.get() == "Магма (Гаммирование)":
        krya = 16
    elif combotext.get() == "Магма (Обратное гаммирование)":
        krya = 17
    elif combotext.get() == "Магма (Имитовставка)":
        krya = 18
    elif combotext.get() == "RSA":
        krya = 19
    elif combotext.get() == "El Gamal":
        krya = 20
    elif combotext.get() == "ГОСТ 34.10-94":
        krya = 21
    elif combotext.get() == "ГОСТ 34.10-2012":
        krya = 22


# Алгоритм шифрования АТБАШ//////////////////////////////////////////////////////////////////////////////////////
def atbash_encrypt():
    alphavite = ',.!:\'\"#?@[](){} '
    #text = message.get()
    global code
    code = ''  # Зашифрованное сообщение
    for i in text:  # блок шифрования
        if i.isupper():
            k = ord(i) % ord('А')  # находим позицию символа в алфавите (начиная с 0)
            code += chr(ord('Я') - k)  # выбираем из алфавита символ, который меньше на k+1 чем длина алфавита
        elif i.islower():
            k = ord(i) % ord('а')
            code += chr(ord('я') - k)
        else:
            code += alphavite[len(alphavite) - alphavite.find(i) - 1]
    messagebox.showinfo("Зашифровка", code)  # Выводим зашифрованное сообщение
    return code

def atbash_decrypt():
    alphavite = ',.!:\'\"#?@[](){} '
    text_decode = code
    if code == '':
        text_decode = text
    global decode
    decode = ''
    for i in text_decode:  # блок расшифрования
        if i.isupper():
            k = ord(i) % ord('А')  # находим позицию символа в алфавите (начиная с 0)
            decode += chr(ord('Я') - k)  # выбираем из алфавита сивол, который меньше на k+1 чем длина алфавита
        elif i.islower():
            k = ord(i) % ord('а')
            decode += chr(ord('я') - k)
        else:
            decode += alphavite[len(alphavite) - alphavite.find(i) - 1]
    messagebox.showinfo("Расшифровка", decode)
    return decode
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Шифр Цезаря////////////////////////////////////////////////////////////////////////////////////////////////////////
def cesar_code():
    global code, key
    alphavite = ',.!:\'\"#?@[](){} '
    alphavite1 = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    alphavite2 = 'АБВГДДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЪЫЬЭЮЯ'
    code = ""
    #text = message.get()
    key = message2.get()
    key = int(key)
    for i in text:
        if i.islower():
            code += alphavite1[(alphavite1.find(i) + key) % len(alphavite1)]
        elif i.isupper():
            code += alphavite2[(alphavite2.find(i) + key) % len(alphavite2)]
        else:
            code += alphavite[(alphavite.find(i) + key) % len(alphavite)]
    messagebox.showinfo("Зашифровка", code)
    # print(code)
def cesar_decode():
    global decode
    alphavite = ',.!:\'\"#?@[](){} '
    alphavite1 = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    alphavite2 = 'АБВГДДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЪЫЬЭЮЯ'
    decode = ""
    key = message2.get()
    key = int(key)
    text_decode = code
    if text_decode == '':
        text_decode = text
    for i in text_decode:
        if i.islower():
            decode += alphavite1[(alphavite1.find(i) - key) % len(alphavite1)]
        elif i.isupper():
            decode += alphavite2[(alphavite2.find(i) - key) % len(alphavite2)]
        else:
            decode += alphavite[(alphavite.find(i) - key) % len(alphavite)]
    messagebox.showinfo("Расшифровка", decode)
    # print(decode)
    return decode
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Шифр Полибия//////////////////////////////////////////////////////////////////////////////////////////////////
def polibiy_crypt():
    alpha = 'абвгдежзийклмнопрстуфхцчшщъыьэюя, .!'  # алфавит
    global code
    code = ''  # Зашифрованное сообщение
    text = message.get().lower()
    for i in text:  # блок шифрования
        code += str(alpha.find(i) // 6 + 1) + str(alpha.find(
            i) % 6 + 1) + ' '  # определяем 2 числа, номер строки, как целое от деления позиции
                            # символа в алфавите на 6, и номер столбца, как остаток от деления позиции символа на 6
    messagebox.showinfo("Зашифровка", code)
def polibiy_decrypt():
    global decode
    alpha = 'абвгдежзийклмнопрстуфхцчшщъыьэюя, .!'
    text_decode = code.split()
    if code == '':
        text_decode = text.split()
    decode = ''
    for i in text_decode:
        decode += alpha[(int(i[0]) - 1) * 6 + int(i[1]) - 1]
    messagebox.showinfo("Расшифровка", decode)

# Шифр Тритемия////////////////////////////////////////////////////////////////////////////////////////////////
def tritemiy_encrypt():
    global code
    alphavite = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'  # алфавит
    alphavite2 = alphavite.upper()
    alphavite3 = ',.!:\'\"#?@[](){} '
    # text = message.get()
    code = ''  # Зашифрованное сообщение
    meow = 0
    for i in text:  # блок шифрования
        if i.islower():
            code += alphavite[(alphavite.find(i) + meow) % len(alphavite)]
        elif i.isupper():
            code += alphavite2[(alphavite2.find(i) + meow) % len(alphavite2)]
        else:
            code += alphavite3[(alphavite3.find(i) + meow) % len(alphavite3)]
        meow += 1
    messagebox.showinfo("Зашифровка", code)
def tritemiy_decrypt():
    global decode
    alphavite = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'  # алфавит
    alphavite2 = alphavite.upper()
    alphavite3 = ',.!:\'\"#?@[](){} '
    decode = ''
    text_decode = code
    if code == '':
        text_decode = text
    meow = 0
    for i in text_decode:
        if i.islower():
            decode += alphavite[(alphavite.find(i) - meow) % len(alphavite)]
        elif i.isupper():
            decode += alphavite2[(alphavite2.find(i) - meow) % len(alphavite2)]
        else:
            decode += alphavite3[(alphavite3.find(i) - meow) % len(alphavite3)]
        meow += 1
    messagebox.showinfo("Расшифровка", decode)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Шифр Белазо////////////////////////////////////////////////////////////////////////////////////////////////
def belazo_encrypt():
    global code, key
    alphavite = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'  # алфавит
    alphavite2 = alphavite.upper()
    alphavite3 = ',.!:\'\"#?@[](){} '
    code = ''
    meow = 0
    # text = message.get()
    key = message2.get()

    for i in text:  # блок шифрования
        if i.islower():
            code += alphavite[(alphavite.find(i) + alphavite.find(key[meow]) + 1) % len(alphavite)]
        elif i.isupper():
            code += alphavite2[(alphavite2.find(i) + alphavite2.find(key[meow].upper()) + 1) % len(alphavite2)]
        else:
            code += alphavite3[(alphavite3.find(i) + alphavite3.find(key[meow]) - 1) % len(alphavite3)]
        meow = (meow + 1) % len(key)
    messagebox.showinfo("Зашифровка", code)
def belazo_decrypt():
    global decode
    alphavite = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'  # алфавит
    alphavite2 = alphavite.upper()
    alphavite3 = ',.!:\'\"#?@[](){} '
    decode = ''
    text_decode = code
    if code == '':
        text_decode = text
    meow = 0

    for i in text_decode:
        if i.islower():
            decode += alphavite[(alphavite.find(i) - alphavite.find(key[meow]) - 1) % len(alphavite)]
        elif i.isupper():
            decode += alphavite2[(alphavite2.find(i) - alphavite2.find(key[meow].upper()) - 1) % len(alphavite2)]
        else:
            decode += alphavite3[(alphavite3.find(i) - alphavite3.find(key[meow]) + 1) % len(alphavite3)]
        meow = (meow + 1) % len(key)
    messagebox.showinfo("Расшифровка", decode)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Шифр Виженера////////////////////////////////////////////////////////////////////////////////////////////////
def viginer_encrypt():
    global code
    alphavite = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'  # алфавит
    alphavite2 = alphavite.upper()
    alphavite3 = ',.!:\'\"#?@[](){} '
    code = ''
    meow = 0
    text = message.get()
    key = message2.get()
    key = key + text
    for i in text:  # блок шифрования
        if i.islower():
            code += alphavite[(alphavite.find(i) + alphavite.find(key[meow])) % len(alphavite)]
        elif i.isupper():
            code += alphavite2[(alphavite2.find(i) + alphavite2.find(key[meow].upper())) % len(alphavite2)]
        else:
            code += alphavite3[(alphavite3.find(i) + alphavite3.find(key[meow])) % len(alphavite3)]
        meow = (meow + 1) % len(key)
    messagebox.showinfo("Зашифровка", code)
def viginer_decrypt():
    alphavite = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'  # алфавит
    alphavite2 = alphavite.upper()
    alphavite3 = ',.!:\'\"#?@[](){} '
    key = message2.get()
    key = key + text
    decode = ''
    if code == '':
        text_decode = text
    else:
        text_decode = code
    meow = 0
    for i in text_decode:
        if i.islower():
            decode += alphavite[(alphavite.find(i) - alphavite.find(key[meow])) % len(alphavite)]
        elif i.isupper():
            decode += alphavite2[(alphavite2.find(i) - alphavite2.find(key[meow].upper())) % len(alphavite2)]
        else:
            decode += alphavite3[(alphavite3.find(i) - alphavite3.find(key[meow])) % len(alphavite3)]
        meow = (meow + 1) % len(key)
    messagebox.showinfo("Расшифровка", decode)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Матричный/////////////////////////////////////////////////////////////////////////////////////////////////

# Проверка условий на ошибки
def checkErrors(key):
    if len(key) != MatrixSquare:
        return "Длина ключа не равна длине квадрата матрицы!!!"    # "len(key) != %d" % MatrixSquare
    elif not getDeter(sliceto(key)):
        return "Определитель матрицы равен 0!!!"
    elif not getDeter(sliceto(key)) % MatrixMod:
        return "Определитель матрицы mod длина алфавита = 0"  # det(Key) mod len(alpha) = 0
    else:
        return None

# Регулярное выражение - 3 символа сообщения
def regular(text):
    template = r".{%d}" % MatrixLength
    return findall(template, text)

# Кодирование символов в матрице
def encode(matrix):
    for x in range(len(matrix)):
        for y in range(MatrixLength):
            matrix[x][y] = alpha.index(matrix[x][y])
    return matrix

# Декодирование чисел в матрице + шифрование/расшифрование
def decode(matrixM, matrixK, message = ""):
    matrixF = []
    for z in range(len(matrixM)):
        temp = [0 for _ in range(MatrixLength)]
        for x in range(MatrixLength):
            for y in range(MatrixLength):
                temp[x] += matrixK[x][y] * matrixM[z][y]
            temp[x] = alpha[temp[x] % MatrixMod]
        matrixF.append(temp)
    for string in matrixF:
        message += "".join(string)
    return message

# Создаёт матрицу по три символа
def sliceto(text):
    matrix = []
    for three in regular(text):
        matrix.append(list(three))
    return encode(matrix)

# Нахождение обратного определителя матрицы
def iDet(det):
    for num in range(MatrixMod):
        if num * det % MatrixMod == 1:
            return num

# Алгебраические дополнения
def algebratic(x, y, det):
    matrix = sliceto(mainKey)
    matrix.remove(matrix[x])
    for z in range(2):
        matrix[z].remove(matrix[z][y])
    det2x2 = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return (pow(-1, x + y) * det2x2 * iDet(det)) % MatrixMod

# Получение определителя матрицы
def getDeter(matrix):
    return \
    (matrix[0][0] * matrix[1][1] * matrix[2][2]) + \
    (matrix[0][1] * matrix[1][2] * matrix[2][0]) + \
    (matrix[1][0] * matrix[2][1] * matrix[0][2]) - \
    (matrix[0][2] * matrix[1][1] * matrix[2][0]) - \
    (matrix[0][1] * matrix[1][0] * matrix[2][2]) - \
    (matrix[1][2] * matrix[2][1] * matrix[0][0])

# Получение алгебраических дополнений
def getAlgbr(det, index = 0):
    algbrs = [0 for _ in range(MatrixSquare)]
    for string in range(MatrixLength):
        for column in range(MatrixLength):
            algbrs[index] = algebratic(string, column, det)
            index += 1
    return algbrs

# Получение обратной матрицы
def getIMatr(algbr):
    return [
        [algbr[0],algbr[3],algbr[6]],
        [algbr[1],algbr[4],algbr[7]],
        [algbr[2],algbr[5],algbr[8]]
    ]

# Основная функция
def encryptDecrypt(mode, message, key):
    MatrixMessage = sliceto(message)
    MatrixKey = sliceto(key)
    if mode == '1':
        final_matrich = decode(MatrixMessage, MatrixKey)
    else:
        algbr = getAlgbr(getDeter(MatrixKey))
        final_matrich = decode(MatrixMessage, getIMatr(algbr))
    return final_matrich
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Шифр Плэйфера/////////////////////////////////////////////////////////////////////////////////////////////////
def playfer_crypt():
    # инициализация алфавита
    alphavite_lower = ['а', 'б', 'в', 'г', 'д',
                       'е', 'ж', 'з', 'и', 'к',
                       'л', 'м', 'н', 'о', 'п',
                       'р', 'с', 'т', 'у', 'ф',
                       'х', 'ц', 'ч', 'ш', 'щ',
                       'ь', 'ы', 'э', 'ю', 'я']

    global  enc_text_final_playf
    enc_text_final_playf = ""
    # text = input(" Введите текст (без пробелов и небуквенных символов): ").lower()  # Вводим текст
    # key = input(" Введите ключ (без повторяющихся символов): ").lower()  # Вводим ключ
    text = message.get().lower()
    for krya in text.lower():
        if krya == ',':
            text = text.replace(krya, 'зпт')
        elif krya == ".":
            text = text.replace(krya, "тчк")
        elif krya not in alphavite_lower:
            text = text.replace(krya, '')

    # Формируем алфавит
    new_alphabet = []  # Заготовка под новый алфавит

    for i in range(len(key)):
        new_alphabet.append(key[i])  # Заполняем новый алфавит значением ключа
    for i in range(len(alphavite_lower)):
        bool_buff = False  # Буфер для проверки вхождения символа в алфавит ниже
        for j in range(len(key)):
            if alphavite_lower[i] == key[j]:
                # Если находим вхождение символа алфавита в ключ, то прерываем цикл и переходим к другому символу
                bool_buff = True
                break
        if bool_buff == False:  # Если не нашли вхождение символа алфавита в ключ, то записываем его в новый алфавит
            new_alphabet.append(alphavite_lower[i])  # Заполняем алфавит
    print(" new_alphabet = {}".format(new_alphabet))

    # Формируем матричный алфавит
    mtx_abt_j = []  # Заготовка под матричный алфавит по j
    counter = 0
    for j in range(5):
        mtx_abt_i = []  # Заготовка под матричный алфавит по i в j
        for i in range(6):
            mtx_abt_i.append(new_alphabet[counter])  # Добавляем букву в матрицу
            counter = counter + 1
        mtx_abt_j.append(mtx_abt_i)
    print(" mtx_abt = {}".format(mtx_abt_j))
    # Поправляем текст
    if len(text) % 2 == 1:  # Если последняя биграмма состоит из одной буквы, то добавляем букву в конец
        text = text + "я"
    print(" text = {}".format(text))
    # Шифруем
    enc_text = ""
    for t in range(0, len(text), 2):
        flag = True  # флаг для выхода из всех циклов
        for j_1 in range(5):
            if flag == False:
                break
            for i_1 in range(6):
                if flag == False:
                    break
                if mtx_abt_j[j_1][i_1] == text[t]:
                    for j_2 in range(5):
                        if flag == False:
                            break
                        for i_2 in range(6):
                            if mtx_abt_j[j_2][i_2] == text[t + 1]:
                                # Если буквы по диагонали
                                if j_1 != j_2 and i_1 != i_2:
                                    enc_text = enc_text + mtx_abt_j[j_1][i_2] + mtx_abt_j[j_2][i_1]
                                # Если буквы на одной строке
                                elif j_1 == j_2 and i_1 != i_2:
                                    enc_text = enc_text + mtx_abt_j[j_1][(i_1 + 1) % 6] + mtx_abt_j[j_2][
                                        (i_2 + 1) % 6]  # %6 для предотвращения выхода за строку
                                # Если буквы в одном столбце
                                elif j_1 != j_2 and i_1 == i_2:
                                    enc_text = enc_text + mtx_abt_j[(j_1 - 1) % 5][i_1] + mtx_abt_j[(j_2 - 1) % 5][
                                        i_2]  # %5 для предотвращения выхода за столбец
                                # Если буквы совпадают
                                elif j_1 == j_2 and i_1 == i_2:
                                    enc_text = enc_text + mtx_abt_j[j_1][i_1] + mtx_abt_j[j_1][i_1]
                                print(" {}{} -> {}{}".format(text[t], text[t + 1], enc_text[t], enc_text[t + 1]))
                                flag = False
                                break
    enc_text_final_playf = "{}".format(enc_text)
    messagebox.showinfo("Зашифровка", enc_text_final_playf)

def playfer_decrypt():
    # инициализация алфавита
    alphavite_lower = ['а', 'б', 'в', 'г', 'д',
                       'е', 'ж', 'з', 'и', 'к',
                       'л', 'м', 'н', 'о', 'п',
                       'р', 'с', 'т', 'у', 'ф',
                       'х', 'ц', 'ч', 'ш', 'щ',
                       'ь', 'ы', 'э', 'ю', 'я']

    # text = input(" Введите текст (без пробелов и небуквенных символов): ").lower()  # Вводим текст
    # key = input(" Введите ключ (без повторяющихся символов): ").lower()  # Вводим ключ
    text = enc_text_final_playf
    if enc_text_final_playf == "":
        text = message.get().lower()
    key = message2.get().lower()
    for kryak in text:
        if kryak == ',':
            text = text.replace(kryak, 'зпт')
        elif kryak == ".":
            text = text.replace(kryak, "тчк")
        elif kryak not in alphavite_lower:
            text = text.replace(kryak, '')

    # Формируем алфавит
    new_alphabet = []  # Заготовка под новый алфавит

    for i in range(len(key)):
        new_alphabet.append(key[i])  # Заполняем новый алфавит значением ключа
    for i in range(len(alphavite_lower)):
        bool_buff = False  # Буфер для проверки вхождения символа в алфавит ниже
        for j in range(len(key)):
            if alphavite_lower[i] == key[j]:
                # Если находим вхождение символа алфавита в ключ, то прерываем цикл и переходим к другому символу
                bool_buff = True
                break
        if bool_buff == False:  # Если не нашли вхождение символа алфавита в ключ, то записываем его в новый алфавит
            new_alphabet.append(alphavite_lower[i])  # Заполняем алфавит
    print(" new_alphabet = {}".format(new_alphabet))

    # Формируем матричный алфавит
    mtx_abt_j = []  # Заготовка под матричный алфавит по j
    counter = 0
    for j in range(5):
        mtx_abt_i = []  # Заготовка под матричный алфавит по i в j
        for i in range(6):
            mtx_abt_i.append(new_alphabet[counter])  # Добавляем букву в матрицу
            counter = counter + 1
        mtx_abt_j.append(mtx_abt_i)
    print(" mtx_abt = {}".format(mtx_abt_j))
    # Поправляем текст
    if len(text) % 2 == 1:  # Если последняя биграмма состоит из одной буквы, то добавляем букву в конец
        text = text + "я"
    print(" text = {}".format(text))
    # Расшифровываем
    enc_text = ""
    for t in range(0, len(text), 2):
        flag = True  # флаг для выхода из всех циклов
        for j_1 in range(5):
            if flag == False:
                break
            for i_1 in range(6):
                if flag == False:
                    break
                if mtx_abt_j[j_1][i_1] == text[t]:
                    for j_2 in range(5):
                        if flag == False:
                            break
                        for i_2 in range(6):
                            if mtx_abt_j[j_2][i_2] == text[t + 1]:
                                # Если буквы по диагонали
                                if j_1 != j_2 and i_1 != i_2:
                                    enc_text = enc_text + mtx_abt_j[j_1][i_2] + mtx_abt_j[j_2][i_1]
                                # Если буквы на одной строке
                                elif j_1 == j_2 and i_1 != i_2:
                                    enc_text = enc_text + mtx_abt_j[j_1][(i_1 - 1) % 6] + mtx_abt_j[j_2][
                                        (i_2 - 1) % 6]  # %6 для предотвращения выхода за строку
                                # Если буквы в одном столбце
                                elif j_1 != j_2 and i_1 == i_2:
                                    enc_text = enc_text + mtx_abt_j[(j_1 + 1) % 5][i_1] + mtx_abt_j[(j_2 + 1) % 5][
                                        i_2]  # %5 для предотвращения выхода за столбец
                                # Если буквы совпадают
                                elif j_1 == j_2 and i_1 == i_2:
                                    enc_text = enc_text + mtx_abt_j[j_1][i_1] + mtx_abt_j[j_1][i_1]
                                print(" {}{} -> {}{}".format(text[t], text[t + 1], enc_text[t], enc_text[t + 1]))
                                flag = False
                                break
    messagebox.showinfo("Расшифровка", "{}".format(enc_text))
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Вертикальная перестановка/////////////////////////////////////////////////////////////////////////////////////
def vertical_change_encrypt_decrypt():
    global encrypted_matrix, split_msg
    alphabet_lower = {'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4,
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

    key = message2.get()
    key_len = len(key)
    # print("Длина ключа:", key_len)
    msg = message.get()
    while len(msg) < key_len * key_len:
        msg += '.'
    # print("Длина фразы:", len(msg))
    msg_pl_key = key + msg
    list_msg = list(msg_pl_key)
    split_msg = [list_msg[i:i + key_len] for i in range(0, len(list_msg), key_len)]
    for i in range(len(split_msg)):
        for j in range(len(split_msg[i])):
            print(split_msg[i][j], end=" ")
        print()
    coded = list()
    for i in range(len(split_msg)):
        for j in range(len(split_msg[i])):
            print(int(alphabet_lower.get(split_msg[i][j])), end=" ")
            coded.append(int(alphabet_lower.get(split_msg[i][j])))
        print()
    split_coded = [coded[i:i + key_len] for i in range(0, len(coded), key_len)]
    # сортировка ключа и шифрование таблицы
    encrypted_matrix = list()
    # print("\nЗашифрованная матрица: ")

    def sortRow(keylen, badlist):
        k = key_len - 1
        while k > 0:
            ind = 0
            for j in range(k + 1):
                if badlist[0][j] > badlist[0][ind]:
                    ind = j
            for i in range(len(badlist)):
                m = badlist[i][ind]
                badlist[i][ind] = badlist[i][k]
                badlist[i][k] = m
            k -= 1
        for i in range(len(badlist)):
            for j in range(keylen):
                # print("%4d" % badlist[i][j], end='')
                encrypted_matrix.append(badlist[i][j])
            # print()

    sortRow(key_len, split_coded)
    split_encrypted = [encrypted_matrix[i:i + key_len] for i in range(0, len(encrypted_matrix), key_len)]
    # print("Зашифрованный текст:", split_encrypted)
    # print("\nЗашифрованный текст: ")

    def get_key(d, value):
        for k, v in d.items():
            if v == value:
                return k

    code = ''
    for i in range(len(split_encrypted)):
        for j in range(len(split_encrypted[i])):
            # print(get_key(alphabet_lower, split_encrypted[i][j]), end=" ")
            code += get_key(alphabet_lower, split_encrypted[i][j])
    # messagebox.showinfo("Зашифровка", code)

    # расшифровка
    decrypted_matrix = list()

    def sortRowDec(keylen, badlist):
        k = keylen - 1
        while k > 0:
            ind = 0
            for j in range(k + 1):
                if badlist[0][j] > badlist[0][ind]:
                    ind = j
            for i in range(len(badlist)):
                m = badlist[i][ind]
                badlist[i][ind] = badlist[i][k]
                badlist[i][k] = m
            k -= 1
            for i in range(len(badlist)):
                for j in range(keylen):
                    print("%4d" % badlist[i][j], end='')
                    decrypted_matrix.append(badlist[i][j])
                print()

    split_decrypted = [encrypted_matrix[i:i + key_len] for i in range(0, len(encrypted_matrix), key_len)]
    sortRowDec(key_len, split_decrypted)
    decode = ""
    for i in range(1, len(split_msg)):
        for j in range(0, len(split_msg[i])):
            decode += split_msg[i][j] + " "

    return code, decode
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Диффи-Хэллман/////////////////////////////////////////////////////////////////////////////////////////////////
def diffie_hellman(p, g, ka, kb):
    change_success = ""
    # p = p = int(input("Введите простое число P: "))        # Простое число
    # g = int(input("Введите натуральное число G: "))  # Натуральное число

    if g ** (p - 1) % p != 1:
        messagebox.showinfo("Ошибка", "Введите другие числа P и G!")
        # raise SystemExit
    else:
        # Секретное число
        # ka = int(input("Введите натуральное (секретное) число Алисы - kа: "))
        # a = 41 Натуральное число Алисы
        # kb = int(input("Введите натуральное (секретное) число Боба - kb: "))
        # b = 12 Натуральное число Боба
        # e = 31 # Натуральное число Евы

        # Открытый ключ
        YA = g ** ka % p  # Алиса
        YB = g ** kb % p  # Боб
        # E = g**e%p   # Ева
        change_success = "Открытый ключ Алисы: " + str(YA) + "\nОткрытый ключ Боба: " + str(YB) + '\n'  # , E

        # Секретный ключ
        K1 = YB ** ka % p  # Key300
        K2 = YA ** kb % p  # Ключ
        # kE = A**e%p     # Key
        change_success += "Приватный ключ Алисы: " + str(K1) + "\nПриватный ключ Боба: " + str(K2)  # , kE
        messagebox.showinfo("Итоги обмена ключами", change_success)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Функции вывода////////////////////////////////////////////////////////////////////////////////////////////////
def proccess_crypt():
    select()
    global text, key, MatrixLength, MatrixMod, MatrixSquare, alpha
    alpha = tuple("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ .,!/{}\'\"1234567890")  # .,!/{}\'\"
    MatrixLength = 3
    MatrixMod = len(alpha)
    MatrixSquare = MatrixLength * MatrixLength
    text = message.get()
    key = message2.get()
    if krya == 1:
        atbash_encrypt()
    elif krya == 2:
       #cesar_code()
       try:
         cesar_code()
       except:
            messagebox.showinfo("Ошибка", "Вы не ввели ключ\nили открытый текст!")
    # messagebox.showinfo("Зашифровка", code)  # Выводим зашифрованное сообщение
    elif krya == 3:
        polibiy_crypt()
    elif krya == 4:
        tritemiy_encrypt()
    elif krya == 5:
        try:
            belazo_encrypt()
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели ключ\nили открытый текст!")
    elif krya == 6:
        try:
            viginer_encrypt()
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели ключ\nили открытый текст!")

    elif krya == 7:   # Матричный шифр////////////////////////////////////////////////////////////////////
        try:
            cryptMode = "1"
            global mainKey, final_matrich
            startMessage = message.get().upper()
            mainKey = message2.get().upper()

            if checkErrors(mainKey):
                messagebox.showinfo("Ошибка!", checkErrors(mainKey))
                raise SystemExit
            for symbol in startMessage:
                if symbol not in alpha:
                    startMessage = startMessage.replace(symbol, '')

            while len(startMessage) % MatrixLength != 0:
                startMessage += startMessage[-1]
            final_matrich = encryptDecrypt(cryptMode, startMessage, mainKey)
            messagebox.showinfo('Зашифровка', final_matrich)
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели ключ\nили открытый текст!")
    elif krya == 8:
        try:
            playfer_crypt()
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели ключ\nили открытый текст!")
    elif krya == 9:
        try:
            otvet_tut = vertical_change_encrypt_decrypt()
            messagebox.showinfo('Расшифровка', otvet_tut[0])
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели ключ\nили открытый текст!")
    elif krya == 10:
        try:
            otvet = reshetka_kardano(int(key), text)
            messagebox.showinfo("Зашифровка", otvet[0])
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели размер матрицы\nили открытый текст!")
    elif krya == 11:
        try:
            otvet_notepad = notepad_shenona(text)
            messagebox.showinfo("Зашифровка", otvet_notepad[0] + "\n" + otvet_notepad[1] + "\n" + otvet_notepad[2])
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели открытый текст!")
    elif krya == 12:
        try:
            otvet_a5 = a5_realisation(text)
            messagebox.showinfo("Зашифровка", otvet_a5[0] + "\n" + otvet_a5[1] + "\n" + otvet_a5[2]
                                + "\n" + otvet_a5[3])
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели открытый текст!")
    elif krya == 13:
        try:
            otvet_a5 = a52_realisation(text)
            messagebox.showinfo("Зашифровка", otvet_a5[0] + "\n" + otvet_a5[1] + "\n" + otvet_a5[2]
                                + "\n" + otvet_a5[3])
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели открытый текст!")
    elif krya == 14:
        try:
            try:
                os.remove("crypted_file.txt")
            except:
                print("Готово к работе!")
            f = open('file.txt', 'w')
            f.write(str(text))
            f.close()
            way = '1'
            AES_realize(way, key)
            f2 = open("crypted_file.txt", 'r')
            otvet = f2.read()
            messagebox.showinfo("Зашифровка", otvet)
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели открытый текст или ключ на английском!")
    elif krya == 15:
        try:
            otvet_magma_prZamena = prZamena(text)
            messagebox.showinfo("Зашифровка", "16-ричное сообщение:" + "\n" + otvet_magma_prZamena[0] + "\n"
                                + "Зашифрованное сообщение:" + "\n" + otvet_magma_prZamena[1] + "\n")
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели открытый текст!")
    elif krya == 16:
        try:
            otvet_magma_gamma = Gamma(text)
            messagebox.showinfo("Зашифровка", "Дополненое сообщение:" + "\n" + otvet_magma_gamma[0] + "\n"
                                + "Зашифрованное сообщение:" + "\n" + otvet_magma_gamma[1])
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели открытый текст!")
    elif krya == 17:
        try:
            otvet_magmaOBR_gamma = GammaOBR(text)
            messagebox.showinfo("Зашифровка", "Дополненое сообщение:" + "\n" + otvet_magmaOBR_gamma[0] + "\n"
                                + "Зашифрованное сообщение:" + "\n" + otvet_magmaOBR_gamma[1])
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели открытый текст!")
    elif krya == 18:
        try:
            otvet_magma_imitovstavka = imitovstavka(text)
            messagebox.showinfo("Зашифровка", "16-ричное сообщение:" + "\n" + otvet_magma_imitovstavka[0] + "\n"
                                + "Имитовставка:" + "\n" + otvet_magma_imitovstavka[1])
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели открытый текст!")
    elif krya == 19:
        try:
            global otvet_rsa
            otvet_rsa = RSA_realisation(text)
            messagebox.showinfo("ЭЦП", otvet_rsa[0])
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели открытый текст!")
    elif krya == 20:
        try:
            global otvet_elGamal
            otvet_elGamal = ElGamal_realisation(text)
            messagebox.showinfo("ЭЦП", otvet_elGamal[0])
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели открытый текст!")
    elif krya == 21:
        try:
            global otvet_Gost_34_10_94
            otvet_Gost_34_10_94 = GOST_34_10_94_realisation(text)
            messagebox.showinfo("ЭЦП", otvet_Gost_34_10_94[0])
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели открытый текст!")
    elif krya == 22:
        global otvet_Gost_34_10_2012
        otvet_Gost_34_10_2012 = GOST_34_10_2012_realisation(text.lower())
        messagebox.showinfo("ЭЦП", otvet_Gost_34_10_2012[0])
        '''try:
            global otvet_Gost_34_10_2012
            otvet_Gost_34_10_2012 = GOST_34_10_2012_realisation(text)
            messagebox.showinfo("ЭЦП", otvet_Gost_34_10_2012[0])
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели открытый текст!")'''
def proccess_decrypt():
    global text, key, MatrixLength, MatrixMod, MatrixSquare, alpha
    alpha = tuple("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ .,!/{}\'\"1234567890")  # .,!/{}\'\"
    MatrixLength = 3
    MatrixMod = len(alpha)
    MatrixSquare = MatrixLength * MatrixLength
    text = message.get()
    key = message2.get()
    if krya == 1:
        atbash_decrypt()
    elif krya == 2:
        try:
            cesar_decode()
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели ключ\nили зашифрованный текст!")
    elif krya == 3:
        polibiy_decrypt()
    elif krya == 4:
        tritemiy_decrypt()
    elif krya == 5:
        try:
            belazo_decrypt()
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели ключ\nили зашифрованный текст!")
    elif krya == 6:
        try:
            viginer_decrypt()
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели ключ\nили зашифрованный текст!")

    elif krya == 7:   # Матричный шифр////////////////////////////////////////////////////////////////////
        try:
            cryptMode = "2"
            global mainKey, startMessage2
            startMessage2 = final_matrich
            if final_matrich == "":
                startMessage2 = message.get().upper()
            mainKey = message2.get().upper()
            if checkErrors(mainKey):
                messagebox.showinfo("Ошибка!", checkErrors(mainKey))
                raise SystemExit
            for symbol in startMessage2:
                if symbol not in alpha:
                    startMessage = startMessage2.replace(symbol, '')

            while len(startMessage2) % MatrixLength != 0:
                startMessage2 += startMessage2[-1]

            messagebox.showinfo('Расшифровка', encryptDecrypt(cryptMode, startMessage2, mainKey))
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели ключ\nили зашифрованный текст!")
    elif krya == 8:
        try:
            playfer_decrypt()
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели ключ\nили зашифрованный текст!")
    elif krya == 9:

        try:
            otvet_tut = vertical_change_encrypt_decrypt()
            messagebox.showinfo('Расшифровка', otvet_tut[1])
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели ключ\nили зашифрованный текст!")
    elif krya == 10:
        try:
            otvet = reshetka_kardano(int(key), text)
            messagebox.showinfo("Зашифровка", otvet[1])
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели размер матрицы\nили открытый текст!")
    elif krya == 11:
        try:
            otvet_notepad = notepad_shenona(text)
            messagebox.showinfo("Зашифровка", otvet_notepad[3] + "\n" + otvet_notepad[4])
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели открытый текст!")
    elif krya == 12:
        try:
            otvet_a5 = a5_realisation(text)
            messagebox.showinfo("Расшифровка", otvet_a5[4] + "\n" + otvet_a5[5])
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели открытый текст!")
    elif krya == 13:
        try:
            otvet_a5 = a52_realisation(text)
            messagebox.showinfo("Расшифровка", otvet_a5[4] + "\n" + otvet_a5[5])
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели открытый текст!")
    elif krya == 14:
        try:
            try:
                os.remove("decrypted_crypted_file.txt")
            except:
                print("Готово к работе!")
            way = '2'
            AES_realize(way, key)
            f2 = open("decrypted_crypted_file.txt", 'r')
            otvet = f2.read()
            messagebox.showinfo("Расшифровка", otvet)
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели открытый текст или ключ на английском!")
    elif krya == 15:
        try:
            otvet_magma_prZamena = prZamena(text)
            messagebox.showinfo("Расшифровка", "Расшифрованное 16-ричное сообщение:" + "\n" + otvet_magma_prZamena[2] + "\n"
                                + "Расшифрованное сообщение:" + "\n" + otvet_magma_prZamena[3])
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели открытый текст!")
    elif krya == 16:
        try:
            otvet_magma_gamma = Gamma(text)
            messagebox.showinfo("Расшифровка", "Расшифрованное сообщение:" + "\n" + otvet_magma_gamma[2])
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели открытый текст!")
    elif krya == 17:
        try:
            otvet_magmaOBR_gamma = GammaOBR(text)
            messagebox.showinfo("Расшифровка", "Расшифрованное сообщение:" + "\n" + otvet_magmaOBR_gamma[2])
        except:
            messagebox.showinfo("Ошибка", "Вы не ввели открытый текст!")
    elif krya == 18:
        messagebox.showinfo("Ошибка", "Имитовставку нельзя расшифровать!")
    elif krya == 19:
        try:
            messagebox.showinfo("Проверка ЭЦП", otvet_rsa[1])
        except:
            messagebox.showinfo("Ошибка", "Сначала нужно создать ЭЦП!\nНажмите зашифровать!")
    elif krya == 20:
        try:
            messagebox.showinfo("Проверка ЭЦП", otvet_elGamal[1])
        except:
            messagebox.showinfo("Ошибка", "Сначала нужно создать ЭЦП!\nНажмите зашифровать!")
    elif krya == 21:
        try:
            messagebox.showinfo("Проверка ЭЦП", otvet_Gost_34_10_94[1])
        except:
            messagebox.showinfo("Ошибка", "Сначала нужно создать ЭЦП!\nНажмите зашифровать!")
    elif krya == 22:
        try:
            messagebox.showinfo("Проверка ЭЦП", otvet_Gost_34_10_2012[1])
        except:
            messagebox.showinfo("Ошибка", "Сначала нужно создать ЭЦП!\nНажмите зашифровать!")
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Очистка значений//////////////////////////////////////////////////////////////////////////////////////////////
def clear_values ():
    global code, decode, key
    code = ''
    decode = ''
    key = ''
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Визуальная часть//////////////////////////////////////////////////////////////////////////////////////////////
root = Tk()
root.title("Алгоритмы шифрования")
root.geometry("470x500+650+150")

text_label1 = "Открытый текст"
label1 = Label(text=text_label1, justify=LEFT)
label1.place(x=200, y=60)

text_label2 = "Ключ"
label2 = Label(text=text_label2, justify=LEFT)
label2.place(x=230, y=120)

message = StringVar()
message2 = StringVar()

message_entry = Entry(textvariable=message, width=40, bd=5)
message_entry.place(x=250, y=100, anchor="c")

message_entry2 = Entry(textvariable=message2, width=20, bd=5)
message_entry2.place(x=250, y=160, anchor="c")

button1 = Button(text="Зашифровать", background="#555", activebackground="#655",
                 foreground="#ccc", padx="20", pady="8", font="16", command=proccess_crypt)
button1.place(x=170, y=190)

button2 = Button(text="Расшифровать", background="#555", activebackground="#655",
                 foreground="#ccc", padx="16", pady="8", font="16", command=proccess_decrypt)
button2.place(x=170, y=250)

button3 = Button(text="Очистить\nзначения", background="#555", activebackground="#655",
                 foreground="#ccc", padx="1", pady="1", font="16", command=clear_values)
button3.place(x=350, y=200)


# Создание формы для диффи-хэллмана/////////////////////////////////////////////////////////////////////////////
def create_form():
    Window()

class Window(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_window()


    def init_window(self):
        p = IntVar()
        g = IntVar()
        ka = IntVar()
        kb = IntVar()
        self.title("Диффи-Хэллман")
        self.geometry("400x400+650+150")
        global P_entry, G_entry, ka_entry, kb_entry
        P_entry = Entry(self, textvariable=p, width=20, bd=5)
        P_entry.place(x=220, y=70, anchor="c")
        G_entry = Entry(self, textvariable=g, width=20, bd=5)
        G_entry.place(x=220, y=130, anchor="c")
        ka_entry = Entry(self, textvariable=ka, width=20, bd=5)
        ka_entry.place(x=220, y=190, anchor="c")
        kb_entry = Entry(self, textvariable=kb, width=20, bd=5)
        kb_entry.place(x=220, y=250, anchor="c")
        self.label_P = Label(self, text="P = ", justify=LEFT)
        self.label_P.place(x=120, y=58)
        self.label_G = Label(self, text="G = ", justify=LEFT)
        self.label_G.place(x=120, y=118)
        self.label_ka = Label(self, text="Секретное число Алисы (натуральное)", justify=LEFT)
        self.label_ka.place(x=115, y=150)
        self.label_kb = Label(self, text="Секретное число Боба (натуральное)", justify=LEFT)
        self.label_kb.place(x=115, y=210)
        button_change = Button(self, text="Обмен ключами", background="#555", activebackground="#655",
                                    foreground="#ccc", padx="20", pady="8", font="16",
                                    command=lambda: diffie_hellman(int(P_entry.get()), int(G_entry.get()), int(ka_entry.get()), int(kb_entry.get())))
        button_change.place(x=133, y=280)


button4 = Button(text="Диффи-Хэллман", background="#555", activebackground="#655",
                 foreground="#ccc", padx="1", pady="1", font="16", command=create_form)
button4.place(x=335, y=470)


vibors = ["Атбаш", "Цезарь", "Полибий", "Тритемий", "Белазо", "Виженер", "Матричный", "Плейфер",
          "Вертикальная перестановка", "Решётка Кардано", "Одноразовый блокнот Шеннона", "A5/1", "A5/2", "AES",
          "Магма (Простая замена)", "Магма (Гаммирование)", "Магма (Обратное гаммирование)", "Магма (Имитовставка)",
          "RSA", "El Gamal", "ГОСТ 34.10-94", "ГОСТ 34.10-2012"]

combotext = StringVar()

combotext.set("Атбаш")

combobox = ttk.Combobox(value=vibors, height=8, width=30, textvariable=combotext, state="readonly")\
    .grid(row=2, sticky=W)

root.mainloop()

# Поговорка
# Эта капуста зеленая, все равно что это зеленая капуста.
