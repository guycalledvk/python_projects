import random as r
numbers = [str(item) for item in range(10)]
lower_letters = [chr(item) for item in range(97, 123)]
upper_letters = [chr(item) for item in range(65, 91)]
symbols = ['.', ',', '/', '?', '<', '>', '*', '$', '#', '@', '!']
lst = [numbers, lower_letters, upper_letters, symbols]
# I am only using symbols I can think of right now
length_of_password = int(input('Enter the length of password you want (minimum 4)... '))
pwd = ''
pwd = pwd + r.choice(numbers) + r.choice(lower_letters) + r.choice(upper_letters) + r.choice(symbols)
temp_count = length_of_password - 4
while temp_count:
    pwd = pwd + r.choice([r.choice(item) for item in lst])
    temp_count -= 1
pwd = [ch for ch in pwd]
r.shuffle(pwd)
pwd = ''.join(pwd)
print('Your random password is:', pwd)