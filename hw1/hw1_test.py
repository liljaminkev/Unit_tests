"""
Test cases for homework 1, Fall 2016
"""
import unittest

from hw1 import *

catalog = [["White shelf board", 18, "shelves", [0,1]],
           ["ShelfTrack", 129, "closet system", []],
           ["Starter Closet Kit", 159, "closet system", [5,2,4]]
           ]

sorted_by_rating = [["Starter Closet Kit", 159, "closet system", [5,2,4]],
                  ["White shelf board", 18, "shelves", [0,1]],
                  ["ShelfTrack", 129, "closet system", []]
                  ]
           

class TestShoppingList(unittest.TestCase):
    """
    Test functions working on a list that represents a list of measured goods
    """

    def testCategoryFound(self):
        """
        A case where there are items in the chosen category
        """
        self.assertEqual(find_category(catalog, "closet system"), [["ShelfTrack", 129, "closet system", []],
                                                                   ["Starter Closet Kit", 159, "closet system", [5,2,4]]]
                                                                   )

    def testCategoryNotFound(self):
        """
        A case where there are no items in the chosen category
        """
        self.assertEqual(find_category(catalog, "drawers"), [])

    def testAverageRating(self):
        """
        Get average rating of item which has reviews
        """
        self.assertAlmostEqual(3.666666667, average_rating(["Starter Closet Kit", 159, "closet system", [5,2,4]]))

    def testAverageRatingNotYetRated(self):
        """
        Get average rating of item which has no reviews
        """
        # remember, math.nan == math.nan returns False
        self.assertTrue(math.isnan(average_rating(["ShelfTrack", 129, "closet system", []])))

    def testIsRated(self):
        """
        Check item with ratings
        """
        self.assertTrue(is_rated(["White shelf board", 18, "shelves", [0,1]]))

    def testIsNotRated(self):
        """
        Check item with no ratingss
        """
        self.assertFalse(is_rated(["ShelfTrack", 129, "closet system", []]))

    def testSortByAverageRating(self):
        """
        Sort from highest rating to lowest rating, with unrated items at the end
        """
        self.assertEqual(sorted_by_rating, sort_by_rating(catalog))
         

if __name__ == "__main__":
    unittest.main()
