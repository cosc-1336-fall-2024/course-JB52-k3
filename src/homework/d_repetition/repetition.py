#returns factor of parameter
def get_factorial(num):
    
    factor = 1
    
    for val in range(1, num + 1):
        factor = factor * val
        
    return factor

#returns sum of odd integers up to parameter
def sum_odd_numbers(num):
    
    index = 0
    total = 0
    
    while index <= num:
        total = total + index * (index % 2)
        index += 1

    return total

#displays menu options
def display_menu():
    print("Repetition Menu")
    print("1) Factorial")
    print("2) Sum Odd Numbers")
    print("3) Exit Application")