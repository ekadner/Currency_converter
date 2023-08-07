def first_screen():
    print('''
    -----------------------------
    WELCOME TO CURRENCY CONVERTER
    -----------------------------
    Please choose an option (1/2):
       1- Dollars to Shekels
       2- Shekels to Dollars\n''')


def currency_choice_2():
    while True:
        try:
            choice_input = input("What currency do you want to convert? ")
            choice = int(choice_input)
            if choice == 1 or choice == 2:
                return choice
            else:
                print("Invalid Choice, please try again")
        except ValueError:
            print("Invalid Choice, please try again")


def amount_input_2():
    while True:
        try:
            user_input = input('Please enter an amount to convert: ')
            amount = float(user_input)
            return amount
        except ValueError:
            print("Invalid Choice, please try again")


def calculate_2(self, amount):
    return self.value * amount


def start_over_2():
    while True:
        try:
            choice_input = input("Do you want to start over? (y/n) ")
            s_over = str(choice_input)
            if s_over == "y" or s_over == "n":
                return s_over
            else:
                print("Invalid Choice, please try again")
        except ValueError:
            print("Invalid Choice, please try again")


results_list = []


def finish_2():
    print('''
Thanks for using our currency converter

Your conversions list:''')
    for x in results_list:
        print(x)


def text_file_2():
    file_name = 'conversion_results.txt'
    with open(file_name, 'w') as file:
        file.write('Your conversions list:\n')
        for item in results_list:
            file.write(item + '\n')
        file.close()
