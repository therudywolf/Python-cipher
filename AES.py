import os
import time
nb = 4  # номер колонки of State (for AES = 4)
nr = 10  # кол-во раундов в цикле шифрования (if nb = 4 nr = 10)
nk = 4  # the key length (in 32-bit words)

# Этот dict будет использоваться в SubBytes ().
hex_symbols_to_int = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

sbox = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
]

inv_sbox = [
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
    0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
    0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
    0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
    0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
    0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
    0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
    0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
    0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
    0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
    0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
    0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
    0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
    0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
]

rcon = [[0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36],
        [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        ]


def encrypt(input_bytes, key):
    """Функция шифрует input_bytes в соответствии с алгоритмом AES (128), используя ключ
    Args:
       input_bytes - список int меньше 255, т.е. список байтов. Длина input_bytes постоянно 16
       ключ - полоска простого текста. Не забудь! Эта же строка используется для расшифровки
    Возвращает:
        Список int
    """

    # давайте подготовим наши входные данные: массив состояний и KeySchedule
    state = [[] for j in range(4)]
    for r in range(4):
        for c in range(nb):
            state[r].append(input_bytes[r + 4 * c])

    key_schedule = key_expansion(key)

    state = add_round_key(state, key_schedule)

    for rnd in range(1, nr):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, key_schedule, rnd)

    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, key_schedule, rnd + 1)

    output = [None for i in range(4 * nb)]
    for r in range(4):
        for c in range(nb):
            output[r + 4 * c] = state[r][c]

    return output


def decrypt(cipher, key):
    """Функция расшифровывает шифр в соответствии с алгоритмом AES (128), используя ключ
    Args:
       cipher - список int меньше 255, т.е. список байтов
       ключ - полоска простого текста. Не забудь! Эта же строка используется для расшифровки
    Возвращает:
        Список int
    """

    # подготовим наш алгоритм ввода данных: массив состояний и KeySchedule
    state = [[] for i in range(nb)]
    for r in range(4):
        for c in range(nb):
            state[r].append(cipher[r + 4 * c])

    key_schedule = key_expansion(key)

    state = add_round_key(state, key_schedule, nr)

    rnd = nr - 1
    while rnd >= 1:
        state = shift_rows(state, inv=True)
        state = sub_bytes(state, inv=True)
        state = add_round_key(state, key_schedule, rnd)
        state = mix_columns(state, inv=True)

        rnd -= 1

    state = shift_rows(state, inv=True)
    state = sub_bytes(state, inv=True)
    state = add_round_key(state, key_schedule, rnd)

    output = [None for i in range(4 * nb)]
    for r in range(4):
        for c in range(nb):
            output[r + 4 * c] = state[r][c]

    return output


def sub_bytes(state, inv=False):
    """Это преобразование заменяет каждый элемент из State на элемент из Sbox
    по алгоритму: в шестнадцатеричном виде элемент из State
    состоят из двух значений: 0x <val1> <val2>. Мы берем элемент от пересечения
    val1-row и val2-column в Sbox и поместите его вместо элемента в State.
    Если дешифрование-преобразование включено (inv == True), он использует InvSbox вместо Sbox.
    Args:
        inv - Если значение == False означает, что функция является преобразованием шифрования.
               True - дешифрование-преобразование
    """

    if inv == False:  # encrypt
        box = sbox
    else:  # decrypt
        box = inv_sbox

    for i in range(len(state)):
        for j in range(len(state[i])):
            row = state[i][j] // 0x10
            col = state[i][j] % 0x10

            # Наш Sbox - это плоский массив, а не библия. Итак, мы используем эту trich, чтобы найти elem:
            # И НЕ меняем список sbox! если хотим чтобы это работало
            box_elem = box[16 * row + col]
            state[i][j] = box_elem

    return state


def shift_rows(state, inv=False):
    """Это преобразование сдвигает строки состояния: второе сдвигается на 1 байт,
    третий сдвигается на 2 байта, четвертый сдвигается на 3 байта. Преобразование не
    коснитесь первого ряда. При преобразовании шифрования используется сдвиг влево, в расшифровке - сдвиг вправо
    Args:
        inv: If value == False означает, что функция находится в режиме шифрования. True - режим дешифрования
    """

    count = 1

    if inv == False:  # encrypting
        for i in range(1, nb):
            state[i] = left_shift(state[i], count)
            count += 1
    else:  # decryptionting
        for i in range(1, nb):
            state[i] = right_shift(state[i], count)
            count += 1

    return state


def mix_columns(state, inv=False):
    """При преобразовании шифрования каждый столбец State умножается на
    фиксированный многочлен a (x) = {03} x ** 3 + {01} x ** 2 + {01} x + {02} в поле Галуа.
    При расшифровке умножается на '(x) = {0b} x ** 3 + {0d} x ** 2 + {09} x + {0e}
    Подробная информация в стандарте AES.
    Args:
        inv: If value == False означает, что функция находится в режиме шифрования. True - режим дешифрования
    """

    for i in range(nb):

        if inv == False:  # encryption
            s0 = mul_by_02(state[0][i]) ^ mul_by_03(
                state[1][i]) ^ state[2][i] ^ state[3][i]
            s1 = state[0][i] ^ mul_by_02(state[1][i]) ^ mul_by_03(
                state[2][i]) ^ state[3][i]
            s2 = state[0][i] ^ state[1][i] ^ mul_by_02(
                state[2][i]) ^ mul_by_03(state[3][i])
            s3 = mul_by_03(state[0][i]) ^ state[1][i] ^ state[2][i] ^ mul_by_02(
                state[3][i])
        else:  # decryption
            s0 = mul_by_0e(state[0][i]) ^ mul_by_0b(state[1][i]) ^ mul_by_0d(
                state[2][i]) ^ mul_by_09(state[3][i])
            s1 = mul_by_09(state[0][i]) ^ mul_by_0e(state[1][i]) ^ mul_by_0b(
                state[2][i]) ^ mul_by_0d(state[3][i])
            s2 = mul_by_0d(state[0][i]) ^ mul_by_09(state[1][i]) ^ mul_by_0e(
                state[2][i]) ^ mul_by_0b(state[3][i])
            s3 = mul_by_0b(state[0][i]) ^ mul_by_0d(state[1][i]) ^ mul_by_09(
                state[2][i]) ^ mul_by_0e(state[3][i])

        state[0][i] = s0
        state[1][i] = s1
        state[2][i] = s2
        state[3][i] = s3

    return state


def key_expansion(key):
    """Составляет список RoundKeys для функции AddRoundKey. Все детали
    об алгоритме есть в стандарте AES
    """

    key_symbols = [ord(symbol) for symbol in key]

    # CipherKey должен содержать 16 символов для заполнения таблицы 4 * 4. Если меньше
    # дополнить ключ "0x01"
    if len(key_symbols) < 4 * nk:
        for i in range(4 * nk - len(key_symbols)):
            key_symbols.append(0x01)

    # сделать CipherKey (который является основой KeySchedule)
    key_schedule = [[] for i in range(4)]
    for r in range(4):
        for c in range(nk):
            key_schedule[r].append(key_symbols[r + 4 * c])

    # Продолжаем заполнять KeySchedule
    for col in range(nk, nb * (nr + 1)):  # col - column number
        if col % nk == 0:
            # взять сдвинутый (col - 1)-й столбец
            tmp = [key_schedule[row][col - 1] for row in range(1, 4)]
            tmp.append(key_schedule[0][col - 1])

            # изменить его элементы, используя Sbox-таблицу, как в SubBytes ...
            for j in range(len(tmp)):
                sbox_row = tmp[j] // 0x10
                sbox_col = tmp[j] % 0x10
                sbox_elem = sbox[16 * sbox_row + sbox_col]
                tmp[j] = sbox_elem

            # и, наконец, сделать XOR из 3 столбцов
            for row in range(4):
                s = (key_schedule[row][col - 4]) ^ (tmp[row]
                                                    ) ^ (rcon[row][int(col / nk - 1)])
                key_schedule[row].append(s)

        else:
            # просто делает XOR из 2 столбцов
            for row in range(4):
                s = key_schedule[row][col - 4] ^ key_schedule[row][col - 1]
                key_schedule[row].append(s)

    return key_schedule


def add_round_key(state, key_schedule, round=0):
    """Это преобразование объединяет State и KeySchedule вместе. Xor
    состояния и RoundSchedule (часть KeySchedule).
    """

    for col in range(nk):
        # nb * round - сдвиг, который указывает начало части KeySchedule
        s0 = state[0][col] ^ key_schedule[0][nb * round + col]
        s1 = state[1][col] ^ key_schedule[1][nb * round + col]
        s2 = state[2][col] ^ key_schedule[2][nb * round + col]
        s3 = state[3][col] ^ key_schedule[3][nb * round + col]

        state[0][col] = s0
        state[1][col] = s1
        state[2][col] = s2
        state[3][col] = s3

    return state


# Небольшой блок полезных функций

def left_shift(array, count):
    """Повернуть массив каждый раз"""

    res = array[:]
    for i in range(count):
        temp = res[1:]
        temp.append(res[0])
        res[:] = temp[:]

    return res


def right_shift(array, count):
    """Rotate the array over count times"""

    res = array[:]
    for i in range(count):
        tmp = res[:-1]
        tmp.insert(0, res[-1])
        res[:] = tmp[:]

    return res


def mul_by_02(num):
    """Функция умножается на 2 в пространстве Галуа"""

    if num < 0x80:
        res = (num << 1)
    else:
        res = (num << 1) ^ 0x1b

    return res % 0x100


def mul_by_03(num):
    """Функция умножается на 3 в пространстве Галуа
    пример: 0x03 * num = (0x02 + 0x01) num = num * 0x02 + num
    Дополнением в поле Galua является XOR операция
    """
    return (mul_by_02(num) ^ num)


def mul_by_09(num):
    return mul_by_02(mul_by_02(mul_by_02(num))) ^ num


def mul_by_0b(num):
    return mul_by_02(mul_by_02(mul_by_02(num))) ^ mul_by_02(num) ^ num


def mul_by_0d(num):
    return mul_by_02(mul_by_02(mul_by_02(num))) ^ mul_by_02(mul_by_02(num)) ^ num


def mul_by_0e(num):
    return mul_by_02(mul_by_02(mul_by_02(num))) ^ mul_by_02(mul_by_02(num)) ^ mul_by_02(num)

# Конец небольшого блока полезных функций


print('Шаг 1:')
while True:
    way = input("Выберите деййствие:\n1) Зашифровать\n2) Расшифровать\n")
    if way not in ['1', '2']:
        print('Ошибка!')
        continue
    else:
        break
print()

print('Шаг 2:')
while True:
    print('Введите полное имя файла: ')
    input_path = os.path.abspath(input())

    if os.path.isfile(input_path):
        break
    else:
        print('Это не файл!')
        continue
print()

print('Шаг 3:')
while True:
    key = input('Введите ваш ключ для зашифровки / расшифровки.\nКлюч должен содержать не более 16 символов.\nПожалуйста, не забывайте это!\n')

    if len(key) > 16:
        print('Слишком длинный ключ!')
        continue

    for symbol in key:
        if ord(symbol) > 0xff:
            print('Этот ключ не сработает!')
            continue

    break
print('\r\nПодождите...')

time_before = time.time()

# Input data
with open(input_path, 'rb') as f:
    data = f.read()

if way == '1':
    crypted_data = []
    temp = []
    for byte in data:
        temp.append(byte)
        if len(temp) == 16:
            crypted_part = encrypt(temp, key)
            crypted_data.extend(crypted_part)
            del temp[:]
    else:
        # padding v1
        # crypted_data.extend(temp)

        # padding v2
        if 0 < len(temp) < 16:
            empty_spaces = 16 - len(temp)
            for i in range(empty_spaces - 1):
                temp.append(0)
            temp.append(1)
            crypted_part = encrypt(temp, key)
            crypted_data.extend(crypted_part)

    out_path = os.path.join(os.path.dirname(input_path),
                            'crypted_' + os.path.basename(input_path))

    # Output data
    with open(out_path, 'xb') as ff:
        ff.write(bytes(crypted_data))

else:  # if way == '2'
    decrypted_data = []
    temp = []
    for byte in data:
        temp.append(byte)
        if len(temp) == 16:
            decrypted_part = decrypt(temp, key)
            decrypted_data.extend(decrypted_part)
            del temp[:]
    else:
        # padding v1
        # decrypted_data.extend(temp)

        # padding v2
        if 0 < len(temp) < 16:
            empty_spaces = 16 - len(temp)
            for i in range(empty_spaces - 1):
                temp.append(0)
            temp.append(1)
            decrypted_part = encrypt(temp, key)

    out_path = os.path.join(os.path.dirname(input_path),
                            'decrypted_' + os.path.basename(input_path))

    # Output data
    with open(out_path, 'xb') as ff:
        ff.write(bytes(decrypted_data))

time_after = time.time()

print('Новый файл здесь:', out_path, '--', time_after - time_before, ' секунд')
print('Если что-то не так проверьте введённый вами ключ!')
