from lists import get_highest_list_value, get_lowest_list_value

def main():
    
    selection = 0
    int_list = []
    
    # prompts menu to user / grabs selection
    while True:
        selection = int(input('MENU\n1 - Display High and Low Values of List\n2 - Exit\nPlease enter menu selection: '))
        if selection == 1 or selection == 2:
            break

    # exits given selection
    if selection == 2:
        exit()
    
    # repeats appending user integer value to list
    # potential break after third iteration
    while True:
        selection = 0
        int_list.append(int(input('Enter integer value for list: ')))
        if len(int_list) > 2:
            while True:
                selection = input('Would you like to enter another value? y/n: ').upper()
                if selection == 'Y' or selection == 'N':
                    break
        if selection == 'N':
            break
    
    # grabs function values using list parameter, prints result, then exits
    high_value = get_highest_list_value(int_list)
    low_value = get_lowest_list_value(int_list)
    print(f'For list {int_list} the highest value is {high_value}, and the lowest value is {low_value}.')
    exit()

if __name__ == '__main__':
    main()