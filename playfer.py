def playfer():
    # инициализация алфавита
    alphavite_lower = ['а', 'б', 'в', 'г', 'д',
                       'е', 'ж', 'з', 'и', 'к',
                       'л', 'м', 'н', 'о', 'п',
                       'р', 'с', 'т', 'у', 'ф',
                       'х', 'ц', 'ч', 'ш', 'щ',
                       'ь', 'ы', 'э', 'ю', 'я']

    text = input(" Введите текст: ").lower()  # Вводим текст
    # Вводим ключ
    key = input(" Введите ключ (без повторяющихся символов): ").lower()

    for krya in text:
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
            # Если находим вхождение символа алфавита в ключ, то прерываем цикл и
            if alphavite_lower[i] == key[j]:
                # переходим к другому символу
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
            # Добавляем букву в матрицу
            mtx_abt_i.append(new_alphabet[counter])
            counter = counter + 1
        mtx_abt_j.append(mtx_abt_i)
    print(" mtx_abt = {}".format(mtx_abt_j))
    # Поправляем текст
    if len(text) % 2 == 1:
        text = text + "я"
    print(" text = {}".format(text))
    # Шифруем
    gav = input("1) Шифровать\n2) Расшифровать\nВыберите цифру:\n")
    if gav == '1':
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
                                        enc_text = enc_text + \
                                            mtx_abt_j[j_1][i_2] + \
                                            mtx_abt_j[j_2][i_1]
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
                                        enc_text = enc_text + \
                                            mtx_abt_j[j_1][i_1] + \
                                            mtx_abt_j[j_1][i_1]
                                    print(
                                        " {}{} -> {}{}".format(text[t], text[t + 1], enc_text[t], enc_text[t + 1]))
                                    flag = False
                                    break
        print(" text = {}".format(enc_text))
    elif gav == '2':
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
                                        enc_text = enc_text + \
                                            mtx_abt_j[j_1][i_2] + \
                                            mtx_abt_j[j_2][i_1]
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
                                        enc_text = enc_text + \
                                            mtx_abt_j[j_1][i_1] + \
                                            mtx_abt_j[j_1][i_1]
                                    print(
                                        " {}{} -> {}{}".format(text[t], text[t + 1], enc_text[t], enc_text[t + 1]))
                                    flag = False
                                    break
        print(" text = {}".format(enc_text))


playfer()
