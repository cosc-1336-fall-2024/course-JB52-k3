#
import dictionary

def menu():
    print("     MENU     \n1-Get p distance matrix\n2-Exit")

def display_result(result):
    
    for row in result:
        for item in row:
            print(str(item).rjust(3, " "), end = " ")
        print(" ")

def get_total_list():
    
    num = int(input("How many list will enter? "))
    index = 0
    total_list = []
    
    while(index < num):
        input_list = input("please enter a comma-separated list: ")
        s_list = input_list.split(",")
        s_list = [value.strip() for value in s_list]
        total_list.append(s_list)
        index += 1
    return total_list

def run_menu():
    
    option = 0
    
    while option != 2:
        menu()
        option = int(input("Please enter selection 1 or 2: "))
        result = []
        
        if option == 1:
            result1 = get_total_list()
            result = dictionary.get_p_distance_matrix(result1)
            display_result(result)
        elif option == 2:
            exit()
        else:
            print("INVALID\nPlease select 1 or 2" )

run_menu()