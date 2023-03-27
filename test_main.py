"""
This is the test for how many hours a week a grocery store is open
"""

from main import GroceryStore
from main import CleaningTime
from main import StockingTime

def test_for_weekly_hours():
    """
    This is for testing 10 hours a day
    """
    assert GroceryStore(10,7).total_hours() == 70

def test_for_cleaning_time():
    """
    This is for testing 15 aisles cleaning for 2 hours each
    """
    cleaning_test1 = CleaningTime(aisles= 15, days= 7, hours= 2)
    assert cleaning_test1 == 210

def test_for_sku_time():
    """
    This tests how long it takes to stock
    """
    sku_test = StockingTime(aisles= 15, item_skus= 100)
    assert sku_test == 1500
