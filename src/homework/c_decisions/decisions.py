#get options ratio and get faculty rating

def get_options_ratio(option, total):
    ratio = option / total
    return ratio

def get_faculty_rating(ratio):
    if ratio >= .9 and ratio < 1:
        return "EXCELLENT"
    elif ratio > .8:
        return "VERY GOOD"
    elif ratio > .7:
        return "GOOD"
    elif ratio > .6:
        return "NEEDS IMPROVEMENT"
    elif ratio > 0 and ratio < .59:
        return "UNACCEPTABLE" 
    
