from random import randint
print("Enter your first word:")
first_word = input().lower()
print("Enter your second word:")
second_word = input().lower()
print("Enter your third word:")
third_word = input().lower()
password = first_word + second_word + third_word
new_word = ""
for letter in password:
  if letter == "a":
    random_number = randint(33,37)
    random_char = chr(random_number)
    new_word = new_word + random_char
  elif letter == "e":
    random_number = randint(38,42)
    random_char = chr(random_number)
    new_word = new_word + random_char
  elif letter == "i":
    random_number = randint(43,47)
    random_char = chr(random_number)
    new_word = new_word + random_char
  elif letter == "o":
    random_number = randint(58,61)
    random_char = chr(random_number)
    new_word = new_word + random_char
  elif letter == "u":
    random_number = randint(91,94)
    random_char = chr(random_number)
    new_word = new_word + random_char
  else:
    new_word = new_word + letter

print(f"Your new password is {new_word}")