def get_lowest_list_value(list):

    low_value = list[0]

    for i in range(len(list)):
        if int(list[i]) <= low_value:
            low_value = list[i]

    return low_value

def get_highest_list_value(list):

    high_value = list[0]

    for i in range(len(list)):
        if int(list[i]) >= high_value:
            high_value = list[i]

    return high_value