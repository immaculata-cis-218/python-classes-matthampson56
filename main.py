"""
Week 8
This is to test how many hours a grocery store is open a week
"""

class GroceryStore:
    """
    bla
    """
    def __init__(self, hours=0, days=0):
        self.__hours = hours
        self.__days = days
        

    def total_hours(self):
        """
        This calculates weekly total hours of operation
        """
        weekly_hours = self.__hours * self.__days
        return weekly_hours

class CleaningTime(GroceryStore):
    """
    This is to see how long it will take to clean the store
    """
    def __init__(self, hours, days, aisles=0):
        self.aisles = aisles
        super().__init__(hours, days)

    def cleaning_hours(self):
        """
        Calculates how many hours it takes to clean a store
        """
        cleaning_time = self.__hours * self.__days * self.aisles
        return cleaning_time

class StockingTime(GroceryStore):
    """
    This calculates how much time it takes to stock an aisle
    """
    def __init__(self, hours, days, aisles=0, item_skus=0):
        self.aisles = aisles
        self.item_skus = item_skus
        super().__init__(hours, days)

    def stocking_time(self):
        """
        Shows how much time someone needs to stock a store
        """
        stocking_time = self.aisles * self.item_skus
        return stocking_time

if __name__ == "__main__":
    ten_hours = GroceryStore(10, 7)
    fifteen_aisles = CleaningTime(2, 7, 15)
    hundred_skus = StockingTime(15, 100)
