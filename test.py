import unittest
from Engine import OrderBook

class TestAddOrder(unittest.TestCase):
    orderBook = OrderBook()

    def test_buy_simple_add(self):
        OrderBook.addOrder("BUY", "ticker1", 100, 15.0)
        order1 = Order("BUY", "ticker1", 100, 15.0)
        self.assertEqual(orderBook.buyOrders, order1, 'the first buy order insert wrongly.')

    def test_buy_cheaper_add(self):

    
    def test_buy_greater_add(self):

    

if __name__ == '__main__':
    unittest.main()
