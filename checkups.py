import re

password = input ("Enter your Password:")
print (len(password)>6)
print(len(password)<20)
print(re.search(r'[!@#$%^&*()]', password))
print(password.isnumeric())
print(password.isupper())
print(password.islower())