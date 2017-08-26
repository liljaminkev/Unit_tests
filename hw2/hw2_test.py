from product import *
from catalog import *
import unittest

#create test item objects
item1 = Product(1001, "White shelf", 18.75, "Shelves", [1,3,7])
item2 = Product(1002, "Box", 2.75, "Storage", [])
item3 = Product(1003, "cube", 3.75, "Storage", [2,4,6])

#create and init a catalog obj
catalog1 = Catalog()
catalog1.add(item1)
catalog1.add(item2)
catalog1.add(item3)

#sorted test list to compare return values
sortedList = [item3, item1, item2]

#class to test product class stored in item
class TestProduct(unittest.TestCase):

    def testAverageRating(self):
        """
        Get average rating of item which has reviews
        """
        self.assertAlmostEqual(3.666666667, item1.average_rating())

    def testAverageRatingNotYetRated(self):
        """
        Get average rating of item which has no reviews
        """
        # remember, math.nan == math.nan returns False
        self.assertTrue(math.isnan(item2.average_rating()))

    def testIsRated(self):
        """
        Check item with ratings
        """
        self.assertTrue(item1.is_rated())

    def testIsNotRated(self):
        """
        Check item with no ratingss
        """
        self.assertFalse(item2.is_rated())

#class used to test catalog objects
class TestCatalog(unittest.TestCase):

#create and init a list to be used for remove method
    def setUp(self):
        global listWithItemToBeDeleted
        listWithItemToBeDeleted = Catalog()
        listWithItemToBeDeleted.add(item1)
        listWithItemToBeDeleted.add(item2)
        listWithItemToBeDeleted.add(item3)

    def testCategoryFound(self):
        """
        A case where there are items in the chosen category
        """
        self.assertEqual(catalog1.find_by_category("Shelves"), [item1])

    def testCategoryNotFound(self):
        """
        A case where there are no items in the chosen category
        """
        self.assertEqual(catalog1.find_by_category("drawers"), [])

    def testSortByAverageRating(self):
        """
        Sort from highest rating to lowest rating, with unrated items at the end
        """
        self.assertEqual(catalog1.sort_by_rating(), sortedList)

    def testSkuNotInList(self):
        #test a sku that is not in list
        self.assertEqual(catalog1.find_by_sku(123), [])

    def testSkuFound(self):
        #test that item1 with sku 1001 is returned sku within list
        self.assertEqual(catalog1.find_by_sku(1001), [item1])

        #test removing an item from a list with three items
    def testRemoveSkuInList(self):
        listWithItemToBeDeleted.remove_by_sku(1002)
        self.assertEqual(listWithItemToBeDeleted.items, [item1, item3])

        #test removing an item that is not in the list.
    def testRemoveSkuNotInList(self):
        listWithItemToBeDeleted.remove_by_sku(1005)
        self.assertEqual(listWithItemToBeDeleted.items, [item1, item2, item3])


if __name__ == "__main__":
    unittest.main()
