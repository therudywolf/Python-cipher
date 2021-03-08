from ec import DSGOST
import random
#инициализация алфавита
alphabet_lower = {'а':0, 'б':1, 'в':2, 'г':3, 'д':4,
                  'е':5, 'ж':6, 'з':7, 'и':8, 'й':9,
                  'к':10, 'л':11, 'м':12, 'н':13, 'о':14,
                  'п':15, 'р':16, 'с':17, 'т':18, 'у':19,
                  'ф':20, 'х':21, 'ц':22, 'ч':23, 'ш':24,
                  'щ':25, 'ъ':26, 'ы':27, 'ь':28, 'э':29,
                  'ю':30, 'я':31, ' ':32, ",":33, ".":34}

def hash_value(p, alpha_code_msg):
    i = 0
    hashing_value = 1
    while i < len(alpha_code_msg):
        hashing_value = (((hashing_value-1) + int(alpha_code_msg[i]))**2) % p
        i += 1
    return hashing_value

def test_gost_sign(msg):
    global sign, d
    msg_list = list(msg)
    alpha_code_msg = list()
    for i in range(len(msg_list)):
        alpha_code_msg.append(int(alphabet_lower.get(msg_list[i])))

    p = 57896044618658097711785492504343953926634992332820282019728792003956564821041
    a = 7
    b = 43308876546767276905765904595650931995942111794451039583252968842033849580414
    x = 2
    y = 4018974056539037503335449422937059775635739389905545080690979365213431566280
    q = 57896044618658097711785492504343953927082934583725450622380973592137631069619
    gost = DSGOST(p, a, b, q, x, y)

    message = hash_value(p, alpha_code_msg)

    d = random.randint(1, q-1)
    sign = gost.sign(message, d)

    public_key_16x = ""
    public_key_point = str(sign[2])
    for i in range(24, len(public_key_point)-1):
        public_key_16x += public_key_point[i]

    public_key = int(public_key_16x, 16)
    print("Открытый ключ:", public_key)
    print("(", sign[0], ",", sign[1], ")")


def test_gost_verify(msg):
    msg_list = list(msg)
    alpha_code_msg = list()
    for i in range(len(msg_list)):
        alpha_code_msg.append(int(alphabet_lower.get(msg_list[i])))

    p = 57896044618658097711785492504343953926634992332820282019728792003956564821041
    a = 7
    b = 43308876546767276905765904595650931995942111794451039583252968842033849580414
    x = 2
    y = 4018974056539037503335449422937059775635739389905545080690979365213431566280
    q = 57896044618658097711785492504343953927082934583725450622380973592137631069619
    gost = DSGOST(p, a, b, q, x, y)

    message = hash_value(p, alpha_code_msg)

    public_key = sign[2]
    is_signed = gost.verify(message, sign, public_key)

    if is_signed == True:
        print("Подпись прошла проверку!")
    else:
        print("Беда! Что-то не так!")


msg = input("Введите текст:").lower()
test_gost_sign(msg)
test_gost_verify(msg)
