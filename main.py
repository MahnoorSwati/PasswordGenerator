#Password Generator Project
import random

password = " "
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for i in range(0,nr_letters+1):
  letter = random.choice(letters)
  password=password+letter

for i in range(0,nr_symbols+1):
  symbol = random.choice(symbols)
  password=password+symbol

for i in range(0,nr_numbers+1):
  number = random.choice(numbers)
  password=password+number

random_password = random.sample(password, len(password))
#random_password is a list of random, non-repeating characters from string password
#converting random_password to a string
password_string = " "

for value in random_password:
  password_string = password_string + value

#printing a random, non-repeating password string
print(password_string)
