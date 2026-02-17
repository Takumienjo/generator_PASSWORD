import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

all = lower + upper + numbers + symbols

pass_length = int(input("Введите длинну пароля: "))

temp = random.choices(all, k=pass_length)

password = ''.join(temp)

print("Ваш пароль:", password)
