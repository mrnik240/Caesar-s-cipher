alphabet_rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet_rus_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alphabet_eng = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
alphabet_eng_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
text = list(input("Введите предложение для шифрования...\t"))
bias = int(input("Введите шаг..."))

for i in range(len(text)):
    if text[i].islower():
        if text[i].isascii():
            n = alphabet_eng.find(text[i])
            text[i] = alphabet_eng[n + bias]
        else:
            n = alphabet_rus.find(text[i])
            text[i] = alphabet_rus[n + bias]
    elif text[i].isupper():
        if text[i].isascii():
            n = alphabet_eng_upper.find(text[i])
            text[i] = alphabet_eng_upper[n + bias]
        else:
            n = alphabet_rus_upper.find(text[i])
            text[i] = alphabet_rus_upper[n + bias]
print("".join(text))
