from re import findall  # метод из модуля для разбиения строки на подстроки

# .,!/{}\'\"
alpha = tuple("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ .,")
MatrixLength = 3
MatrixMod = len(alpha)
MatrixSquare = MatrixLength * MatrixLength


# Проверка условий на ошибки
def checkErrors(key):
    if len(key) != MatrixSquare:
        # "len(key) != %d" % MatrixSquare
        return "Error: Длина ключа не равна длине квадрата матрицы!!!"
    elif not getDeter(sliceto(key)):
        return "Error: Определитель матрицы равен 0!!!"
    elif not getDeter(sliceto(key)) % MatrixMod:
        # det(Key) mod len(alpha) = 0
        return "Error: Определитель матрицы mod длина алфавита = 0"
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


def decode(matrixM, matrixK, message=""):
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


def getAlgbr(det, index=0):
    algbrs = [0 for _ in range(MatrixSquare)]
    for string in range(MatrixLength):
        for column in range(MatrixLength):
            algbrs[index] = algebratic(string, column, det)
            index += 1
    return algbrs

# Получение обратной матрицы


def getIMatr(algbr):
    return [
        [algbr[0], algbr[3], algbr[6]],
        [algbr[1], algbr[4], algbr[7]],
        [algbr[2], algbr[5], algbr[8]]
    ]


cryptMode = input(
    "Что будем делать? Введите цифру\n 1) Зашифровать\n 2) Расшифровать\n").upper()
if cryptMode not in ['1', '2']:
    print("Error: mode is not Found")
    raise SystemExit

startMessage = input("Введите текст: ").upper()
mainKey = input("Введите ключ: ").upper()

if checkErrors(mainKey):
    print(checkErrors(mainKey))
    raise SystemExit

for symbol in startMessage:
    if symbol not in alpha:
        startMessage = startMessage.replace(symbol, '')

while len(startMessage) % MatrixLength != 0:
    startMessage += startMessage[-1]

# Основная функция


def encryptDecrypt(mode, message, key):
    MatrixMessage = sliceto(message)
    MatrixKey = sliceto(key)
    if mode == '1':
        final = decode(MatrixMessage, MatrixKey)
    else:
        algbr = getAlgbr(getDeter(MatrixKey))
        final = decode(MatrixMessage, getIMatr(algbr))
    return final


print("Final message:", encryptDecrypt(cryptMode, startMessage, mainKey))
