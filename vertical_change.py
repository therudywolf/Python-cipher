alphabet_lower = {'а':0, 'б':1, 'в':2, 'г':3, 'д':4,
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

key = input("Введите ключ:")
key_len = len(key)
print("Длина ключа:", key_len)
msg = input("Введите текст:")
while len(msg) < key_len * key_len:
	msg += '.'
print("Длина фразы:", len(msg))
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
print("\nЗашифрованная матрица: ")


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
			print("%4d" % badlist[i][j], end='')
			encrypted_matrix.append(badlist[i][j])
		print()


sortRow(key_len, split_coded)
split_encrypted = [encrypted_matrix[i:i + key_len] for i in range(0, len(encrypted_matrix), key_len)]
# print("Зашифрованный текст:", split_encrypted)
print("\nЗашифрованный текст: ")


def get_key(d, value):
	for k, v in d.items():
		if v == value:
			return k


for i in range(1, len(split_encrypted)):
	for j in range(0, len(split_encrypted[i])):
		print(get_key(alphabet_lower, split_encrypted[i][j]), end=" ")

print("\n")
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
print("\nРасшифровка:")
for i in range(1, len(split_msg)):
	for j in range(0, len(split_msg[i])):
		decode += split_msg[i][j] + " "
print(decode)
#print("Расшифрованный текст:", split_msg)
