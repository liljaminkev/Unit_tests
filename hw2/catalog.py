from product import *
#used to hold a collection of products from product.py
class Catalog:
    #constructor that creates item array
    def __init__(self):
        self.items = []

    #appends product to items catalog
    def add(self, item):
        self.items.append(item)

    #return filtered list of items for a given category else return empty list
    def find_by_category(self, categoryIn):
        return list(filter(lambda item: item.category == categoryIn, self.items))

    #return filtered list by sku else return empty list
    def find_by_sku(self, sku):
        return list(filter(lambda item: item.sku == sku, self.items))

    #remove item by sku by itterating through item in items
    def remove_by_sku(self, sku):
        for item in self.items:
            if item.sku == sku:
                self.items.remove(item)

    #return list by sorted ratings with empty ratings at end
    def sort_by_rating(self):
        return list(sorted(filter(lambda item: item.is_rated(), self.items), key=lambda item : item.average_rating(), reverse=True)) + \
               list(filter(lambda item: not item.is_rated(), self.items))
