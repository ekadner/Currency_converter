from functions import first_screen, currency_choice_2, amount_input_2,\
    calculate_2, start_over_2, finish_2, results_list, text_file_2
from USD import Dollar
from SHEKELS import Shekel


first_screen()
while True:
    choice = currency_choice_2()
    if choice == 1:
        print("Dollars to Shekels")
        amount = amount_input_2()
        d_result = calculate_2(Dollar, amount)
        d_result = round(d_result, 1)
        results_list.append(f"{amount} Dollars = {d_result} Shekels")
        print(f"{amount} Dollars = {d_result} Shekels")
    elif choice == 2:
        print("Shekels to Dollars")
        amount = amount_input_2()
        s_result = calculate_2(Shekel, amount)
        s_result = round(s_result, 1)
        results_list.append(f"{amount} Shekels = {s_result} Dollars")
        print(f"{amount} Shekels = {s_result} Dollars")
    s_over = start_over_2()
    if s_over == "y":
        continue
    elif s_over == "n":
        finish_2()
        text_file_2()
    break
