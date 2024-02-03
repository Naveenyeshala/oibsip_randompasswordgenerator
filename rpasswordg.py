import random
import string

lower=string.ascii_lowercase
upper=string.ascii_uppercase
digit=string.digits
symbol=string.punctuation

lower_len=int(input("Enter no.of lowercase characters you want in password\n"))
upper_len=int(input("Enter no.of uppercase characters you want in password\n"))
digit_len=int(input("Enter no.of digits you want in password\n"))
symbol_len=int(input("Enter no.of symbols you want in password\n"))

password_list=[]
for i in range(1,lower_len+1):
    char = random.choice(lower)
    password_list+=char

for i in range(1,upper_len+1):
    char = random.choice(upper)
    password_list+=char

for i in range(1,digit_len+1):
    char = random.choice(digit)
    password_list+=char

for i in range(1,symbol_len+1):
    char = random.choice(symbol)
    password_list+=char
    
# print(password_list)


random.shuffle(password_list)
# print(password_list)
password=""
for char in password_list:
    password+=char
print(password)
