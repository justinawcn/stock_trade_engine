import unittest
from Engine import OrderBook, Order

class TestAddOrder(unittest.TestCase):

    def test_buy_simple_add(self):
        orderBook = OrderBook()
        OrderBook.addOrder(orderBook, "BUY", "ticker1", 100, 15.0)
        self.assertEqual(orderBook.buyOrders.OrderType, "BUY", 'the first buy order insert wrongly. (ordertype)')
        self.assertEqual(orderBook.buyOrders.TickerSymbol, "ticker1", 'the first buy order insert wrongly. (tickersymbol)')
        self.assertEqual(orderBook.buyOrders.Qty, 100, 'the first buy order insert wrongly. (quantity)')
        self.assertEqual(orderBook.buyOrders.Price, 15.0, 'the first buy order insert wrongly. (price)')


    def test_buy_cheaper_add(self):
        orderBook = OrderBook()
        OrderBook.addOrder(orderBook, "BUY", "ticker1", 100, 15.0)
        OrderBook.addOrder(orderBook, "BUY", "ticket1", 80, 10.0)
        self.assertEqual(orderBook.buyOrders.OrderType, "BUY", 'the first buy order insert wrongly. (ordertype)')
        self.assertEqual(orderBook.buyOrders.TickerSymbol, "ticker1", 'the first buy order insert wrongly. (tickersymbol)')
        self.assertEqual(orderBook.buyOrders.Qty, 100, 'the first buy order insert wrongly. (quantity)')
        self.assertEqual(orderBook.buyOrders.Price, 15.0, 'the first buy order insert wrongly. (price)')
  
    
    def test_buy_greater_add(self):
        orderBook = OrderBook()
        OrderBook.addOrder(orderBook, "BUY", "ticket1", 80, 10.0)
        OrderBook.addOrder(orderBook, "BUY", "ticker2", 100, 15.0)
        self.assertEqual(orderBook.buyOrders.OrderType, "BUY", 'the first buy order insert wrongly. (ordertype)')
        self.assertEqual(orderBook.buyOrders.TickerSymbol, "ticker2", 'the first buy order insert wrongly. (tickersymbol)')
        self.assertEqual(orderBook.buyOrders.Qty, 100, 'the first buy order insert wrongly. (quantity)')
        self.assertEqual(orderBook.buyOrders.Price, 15.0, 'the first buy order insert wrongly. (price)')

    
    def test_buy_greater_add_reverse(self):
        orderBook = OrderBook()
        OrderBook.addOrder(orderBook, "BUY", "ticker2", 100, 15.0)
        OrderBook.addOrder(orderBook, "BUY", "ticket1", 80, 10.0)
        self.assertEqual(orderBook.buyOrders.OrderType, "BUY", 'the first buy order insert wrongly. (ordertype)')
        self.assertEqual(orderBook.buyOrders.TickerSymbol, "ticker2", 'the first buy order insert wrongly. (tickersymbol)')
        self.assertEqual(orderBook.buyOrders.Qty, 100, 'the first buy order insert wrongly. (quantity)')
        self.assertEqual(orderBook.buyOrders.Price, 15.0, 'the first buy order insert wrongly. (price)')


    def test_buy_greater_add_231(self):
        orderBook = OrderBook()
        OrderBook.addOrder(orderBook, "BUY", "ticker1", 100, 15.0)
        OrderBook.addOrder(orderBook, "BUY", "ticker3", 75, 20.0)
        OrderBook.addOrder(orderBook, "BUY", "ticket2", 80, 10.0)
        self.assertEqual(orderBook.buyOrders.OrderType, "BUY", 'the first buy order insert wrongly. (ordertype)')
        self.assertEqual(orderBook.buyOrders.TickerSymbol, "ticker3", 'the first buy order insert wrongly. (tickersymbol)')
        self.assertEqual(orderBook.buyOrders.Qty, 75, 'the first buy order insert wrongly. (quantity)')
        self.assertEqual(orderBook.buyOrders.Price, 20.0, 'the first buy order insert wrongly. (price)')


    def test_sell_simple_add(self):
        orderBook = OrderBook()
        OrderBook.addOrder(orderBook, "SELL", "ticker1", 100, 15.0)
        self.assertEqual(orderBook.sellOrders.OrderType, "SELL", 'the first buy order insert wrongly. (ordertype)')
        self.assertEqual(orderBook.sellOrders.TickerSymbol, "ticker1", 'the first buy order insert wrongly. (tickersymbol)')
        self.assertEqual(orderBook.sellOrders.Qty, 100, 'the first buy order insert wrongly. (quantity)')
        self.assertEqual(orderBook.sellOrders.Price, 15.0, 'the first buy order insert wrongly. (price)')


    def test_sell_greater_add(self):
        orderBook = OrderBook()
        OrderBook.addOrder(orderBook, "SELL", "ticker2", 100, 15.0)
        OrderBook.addOrder(orderBook, "SELL", "ticker1", 110, 20.0)
        self.assertEqual(orderBook.sellOrders.OrderType, "SELL", 'the first buy order insert wrongly. (ordertype)')
        self.assertEqual(orderBook.sellOrders.TickerSymbol, "ticker2", 'the first buy order insert wrongly. (tickersymbol)')
        self.assertEqual(orderBook.sellOrders.Qty, 100, 'the first buy order insert wrongly. (quantity)')
        self.assertEqual(orderBook.sellOrders.Price, 15.0, 'the first buy order insert wrongly. (price)')


    def test_sell_greater_add_reverse(self):
        orderBook = OrderBook()
        OrderBook.addOrder(orderBook, "SELL", "ticker1", 110, 20.0)
        OrderBook.addOrder(orderBook, "SELL", "ticker2", 100, 15.0)
        self.assertEqual(orderBook.sellOrders.OrderType, "SELL", 'the first buy order insert wrongly. (ordertype)')
        self.assertEqual(orderBook.sellOrders.TickerSymbol, "ticker2", 'the first buy order insert wrongly. (tickersymbol)')
        self.assertEqual(orderBook.sellOrders.Qty, 100, 'the first buy order insert wrongly. (quantity)')
        self.assertEqual(orderBook.sellOrders.Price, 15.0, 'the first buy order insert wrongly. (price)')


    def test_sell_greater_add_213(self):
        orderBook = OrderBook()
        OrderBook.addOrder(orderBook, "SELL", "ticker2", 110, 20.0)
        OrderBook.addOrder(orderBook, "SELL", "ticker1", 100, 15.0)
        OrderBook.addOrder(orderBook, "SELL", "ticker3", 70, 25.0)
        self.assertEqual(orderBook.sellOrders.OrderType, "SELL", 'the first buy order insert wrongly. (ordertype)')
        self.assertEqual(orderBook.sellOrders.TickerSymbol, "ticker1", 'the first buy order insert wrongly. (tickersymbol)')
        self.assertEqual(orderBook.sellOrders.Qty, 100, 'the first buy order insert wrongly. (quantity)')
        self.assertEqual(orderBook.sellOrders.Price, 15.0, 'the first buy order insert wrongly. (price)')

if __name__ == '__main__':
    unittest.main()
