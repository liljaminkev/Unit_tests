import math
def find_category(catalog, category):
    found = []
    for item in catalog:
        if item[2] == category:
            found.append(item)
    return found
    
def is_rated(item):
    if item[3]:
        return True
    else:
        return False

def average_rating(item):
    if item[3]:
        average = 0
        for rating in item[3]:
            average += rating
        average = average / len(item[3])
        return average
    else:
        return math.nan
def sort_by_rating(catalog):
    return sorted(catalog, key=lambda item: item[3], reverse = True)
        
    