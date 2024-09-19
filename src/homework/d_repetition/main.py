from repetition import display_menu, get_factorial, sum_odd_numbers

def main():
    
    menu_selection = 0
    cont = "y"

    while menu_selection != 3 and cont == "y":
        
        display_menu()

        menu_selection = 0
        func_out = False # variable for loop exit

        # prompts for user selection + verifies acceptable value
        while menu_selection < 1 or menu_selection > 3:
            menu_selection = int(input("Please Enter Menu Selection # : "))

        while menu_selection != 3 and func_out == False:
            
            if menu_selection == 1: # factorial
                fact_input = int(input("Please Enter Number 1-9 : ")) # prompts + input to be factored
                if fact_input > 0 and fact_input < 10: # verify value is acceptable
                    factor = get_factorial(fact_input) # calls function with input parameter
                    print(f"The factor of {fact_input} is {factor}") # displays function output
                    func_out = True # ends loop
                else:
                    print("Invalid Value") # displays error
            
            elif menu_selection == 2: # sum odd numbers
                sum_input = int(input("Please Enter Number 1-99: ")) #prompts + input to be summed
                if sum_input > 0 and sum_input < 100: # verify value is acceptable
                    odd_sum = sum_odd_numbers(sum_input) # calls function with input parameter
                    print(f"The sum of all odd numbers up to {sum_input} is {odd_sum}") # displays function output
                    func_out = True # ends loop
                else:
                    print("Invalid Value") # displays error

        if menu_selection != 3:
            cont = str(input("Make Another Selection? y/n : ")) # prompts to continue program

    print("Application Closed") # on exit notifies user of application status

main()