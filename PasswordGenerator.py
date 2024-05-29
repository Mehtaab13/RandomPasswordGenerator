import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input(f"How many symbols would you like? \n"))
nr_numbers = int(input(f"How many numbers would you like? \n"))
choices = [letters, numbers, symbols]
sequence = ""
for n in range(0, nr_letters + nr_symbols + nr_numbers):
    if nr_letters > 0 and nr_symbols > 0 and nr_numbers > 0:
        choice = random.randint(0, 2)
        option = random.randint(0, len(choices[choice]) - 1)
        sequence += choices[choice][option]
        if choice == 0:
            nr_letters -= 1
        elif choice == 1:
            nr_numbers -= 1
        else:
            nr_symbols -= 1
    elif nr_letters > 0 and nr_symbols > 0:
        new_choices = [letters, symbols]
        choice = random.randint(0, 1)
        option = random.randint(0, len(new_choices[choice]) - 1)
        sequence += new_choices[choice][option]
        if choice == 0:
            nr_letters -= 1
        elif choice == 2:
            nr_numbers -= 1
        else:
            nr_symbols -= 1
    elif nr_letters > 0 and nr_numbers > 0:
        new_choices = [letters, numbers]
        choice = random.randint(0, 1)
        option = random.randint(0, len(new_choices[choice]) - 1)
        sequence += new_choices[choice][option]
        if choice == 0:
            nr_letters -= 1
        elif choice == 1:
            nr_numbers -= 1
        else:
            nr_symbols -= 1
    elif nr_symbols > 0 and nr_numbers > 0:
        new_choices = [symbols, numbers]
        choice = random.randint(0, 1)
        option = random.randint(0, len(new_choices[choice]) - 1)
        sequence += new_choices[choice][option]
        if choice == 2:
            nr_letters -= 1
        elif choice == 1:
            nr_numbers -= 1
        else:
            nr_symbols -= 1
    elif nr_numbers > 0:
        option = random.randint(0, len(numbers) - 1)
        sequence += numbers[option]
        nr_numbers -= 1
    elif nr_symbols > 0:
        option = random.randint(0, len(symbols) - 1)
        sequence += symbols[option]
        nr_symbols -= 1
    elif nr_letters > 0:
        option = random.randint(0, len(letters) - 1)
        sequence += letters[option]
        nr_letters -= 1
print(sequence)
