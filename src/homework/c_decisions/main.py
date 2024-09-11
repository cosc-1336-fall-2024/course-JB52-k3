#get options ratio and get faculty rating

import decisions

def main():
   option = int(input("ENTER OPTION: "))
   total = int(input("ENTER TOTAL: "))
   
   result1 = decisions.get_options_ratio(option, total)
   result2 = decisions.get_faculty_rating(result1)
   print("RATIO: ", '%.2f'%result1)
   print("RATING: ", result2)

main()