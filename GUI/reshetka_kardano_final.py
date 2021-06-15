import random

def reshetka_kardano(SIZE, text):
    matrix_number = 1
    # SIZE = int(input(" Введите размер матрицы (одно число): "))  # вводим размер матрицы XxY
    # text = input(" Введите текст: ")  # вводим текст
    # дополняем матрицу с текстом до полной матрицы
    open_text_ = text
    if len(text) % (SIZE * SIZE) != 0:
        add_number = SIZE * SIZE - len(text) % (SIZE * SIZE)
        for i in range(add_number):
            text = text + "*"
    # определяем количество матриц
    if len(text) / (SIZE * SIZE) != 1:
        matrix_number = int(len(text) / (SIZE * SIZE))
    # print(" Введите значения ячеек решётки Кардано (0 - заполнена, 1 - пустота):\n")

    # формируем решётку Кардано
    bin_matrix = [[0 for x in range(SIZE)] for y in range(SIZE)]
    for i in range(SIZE):
        for j in range(SIZE):
            bin_matrix[i][j] = random.randint(0, 1)   # рандомизируем ячейки матрицы, либо 1, либо 0
            """
            while True:
                bin_matrix[i][j] = int(input(" bin_matrix[{}][{}] = ".format(i, j)))  # вводим значения пустоты/наполнения
                if bin_matrix[i][j] != 0 and bin_matrix[i][j] != 1:
                    print(" Неправильное число!")
                else:
                    break"""
    # формируем матрицу с текстом
    text_matrix = [[[0 for x in range(SIZE)] for y in range(SIZE)] for matrix in range(matrix_number)]
    counter_text = 0  # счётчик позиции символа в тексте
    for i in range(matrix_number):
        for j in range(SIZE):
            for k in range(SIZE):
                text_matrix[i][j][k] = text[counter_text]
                counter_text += 1

    # шифрование
    # SIZE - размерность матрицы, z - номер матрицы с текстом, i - строка (Y), j - столбец (X).
    enc_text = ""
    for z in range(matrix_number):
        # прямой обход решетки
        for i in range(SIZE):
            for j in range(SIZE):
                if bin_matrix[i][j] == 1:
                    enc_text = enc_text + text_matrix[z][i][j]
        # поворот решетки на 90 градусов по часовой стрелке
        for i in range(SIZE):
            for j in range(SIZE):
                if bin_matrix[SIZE - j - 1][i] == 1:
                    enc_text = enc_text + text_matrix[z][i][j]
        # поворот решетки на 180 градусов по часовой стрелке
        for i in range(SIZE):
            for j in range(SIZE):
                if bin_matrix[SIZE - i - 1][SIZE - j - 1] == 1:
                    enc_text = enc_text + text_matrix[z][i][j]
        # поворот решетки на 270 градусов по часовой стрелке
        for i in range(SIZE):
            for j in range(SIZE):
                if bin_matrix[j][SIZE - i - 1] == 1:
                    enc_text = enc_text + text_matrix[z][i][j]
    encrypted_text = str((" {}\n".format(enc_text)))
    # расшифрование
    # формируем матрицу с текстом
    text_matrix = [[[0 for x in range(SIZE)] for y in range(SIZE)] for matrix in range(matrix_number)]
    counter_text = 0  # счётчик позиции символа в тексте
    for i in range(matrix_number):
        for j in range(SIZE):
            for k in range(SIZE):
                text_matrix[i][j][k] = enc_text[counter_text]
                counter_text += 1
    open_text = ""
    for z in range(matrix_number):
        # прямой обход решетки
        for i in range(SIZE):
            for j in range(SIZE):
                if bin_matrix[i][j] == 1:
                    open_text = open_text + text_matrix[z][i][j]
        # поворот решетки на 90 градусов по часовой стрелке
        for i in range(SIZE):
            for j in range(SIZE):
                if bin_matrix[SIZE - j - 1][i] == 1:
                    open_text = open_text + text_matrix[z][i][j]
        # поворот решетки на 180 градусов по часовой стрелке
        for i in range(SIZE):
            for j in range(SIZE):
                if bin_matrix[SIZE - i - 1][SIZE - j - 1] == 1:
                    open_text = open_text + text_matrix[z][i][j]
        # поворот решетки на 270 градусов по часовой стрелке
        for i in range(SIZE):
            for j in range(SIZE):
                if bin_matrix[j][SIZE - i - 1] == 1:
                    open_text = open_text + text_matrix[z][i][j]
    decrypted_text = str(" {}\n".format(open_text_))
    return encrypted_text, decrypted_text
"""size = int(input(" Введите размер матрицы (одно число): "))  # вводим размер матрицы XxY
text = input(" Введите текст: ")  # вводим текст
otvet = reshetka_kardano(size, text)
print(otvet[0], otvet[1])"""
