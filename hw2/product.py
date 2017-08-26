import statistics
import math

class Product:
#constructor takes 6 vars that describe an item and assigns it's vars
    def __init__(self, sku, name, price, category, ratings):
        self.sku = sku
        self.name = name
        self.price = price
        self.category = category
        self.ratings = ratings

#check if ratings is not empty. !empty true else false
    def is_rated(self):
        if self.ratings:
            return True
        else:
            return False

#return avg if there exists one else nan
    def average_rating(self):
        if self.ratings:
            return statistics.mean(self.ratings)
        else:
            return math.nan
