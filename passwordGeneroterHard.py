## generate password with suffule the number , symbols and letters


import random
#Imports Python’s built-in random module so you can pick random items (random.choice) and shuffle lists (random.shuffle).

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '#', '$', '%', '(',')','*', '+']
# Three lists holding the possible characters for the password:
# letters contains lowercase + uppercase alphabet letters.
# numbers contains digit characters '0'–'9'.
# symbols contains allowed special characters.

print("Welcome to Password Generator !")
#Prints a welcome message for the user.

n_letter = int(input("How many letters you want to your password ?\n"))
n_symbol = int(input("How many symbol you want to your password ?\n"))
n_number = int(input("How many number you want to your password ?\n"))
# Asks the user how many letters, symbols and numbers they want in the password.
# input() returns a string; int() converts that string into an integer. If the user types something non-numeric this will raise a ValueError.

password_list = []  # we use list except the string because in list , we have suffule function to suffule the password
# Creates an empty list that will hold chosen characters.
# You use a list here because random.shuffle() works in-place on lists (and because it’s easy to join list items into a string later).

for i in range(1,n_letter+1):
    char1 = random.choice(letters)
    password_list += char1
# Loop runs n_letter times (from 1 to n_letter inclusive).
# random.choice(letters) picks a random element from the letters list.
# password_list += char1 appends the chosen character to password_list.
# Note: password_list += char1 works because char1 is a single-character string — it extends the list with that single character. More idiomatic would be password_list.append(char1).

for i in range(1,n_symbol+1):
    char2 = random.choice(symbols)
    password_list += char2
#Same pattern as above, but picks n_symbol random symbols and adds them to password_list.

for i in range(1,n_number+1):
    char3 = random.choice(numbers)
    password_list += char3
#Same pattern again, adds n_number random digits.


random.shuffle(password_list)   # it shuffle the original password list 
#Shuffles the elements of password_list in place, so letters, symbols and numbers are mixed randomly rather than grouped by type.

password = ''
#Creates an empty string which will hold the final password.

for char in password_list:
    password += char
# Iterates over each character in the shuffled list and concatenates it to password. At the end, password is a single string with all characters in random order.
# Slightly more efficient and idiomatic alternative: password = ''.join(password_list).

print(password)
#Prints the generated, shuffled password to the user.