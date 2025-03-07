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

    def test_one_no_match(self):
        orderBook = OrderBook()
        OrderBook.addOrder(orderBook, "BUY", "ticker1", 100, 50.0)
        OrderBook.addOrder(orderBook, "SELL", "ticker1", 110, 20.0)

        self.assertEqual(orderBook.buyOrders.OrderType, "BUY", 'buy order after match. (ordertype)')
        self.assertEqual(orderBook.buyOrders.TickerSymbol, "ticker1", 'buy order after match. (tickersymbol)')
        self.assertEqual(orderBook.buyOrders.Qty, 100, 'buy order after match. (quantity)')
        self.assertEqual(orderBook.buyOrders.Price, 50.0, 'buy order after match. (price)')

        self.assertEqual(orderBook.sellOrders.OrderType, "SELL", 'sell order after match. (ordertype)')
        self.assertEqual(orderBook.sellOrders.TickerSymbol, "ticker1", 'sell order after match. (tickersymbol)')
        self.assertEqual(orderBook.sellOrders.Qty, 110, 'sell order after match. (quantity)')
        self.assertEqual(orderBook.sellOrders.Price, 20.0, 'sell order after match. (price)')

    def test_fully_match(self):
        orderBook = OrderBook()
        OrderBook.addOrder(orderBook, "BUY", "ticker1", 150, 50.0)
        OrderBook.addOrder(orderBook, "SELL", "ticker1", 150, 20.0)

        OrderBook.matchOrder(orderBook, "ticker1")

        self.assertEqual(orderBook.buyOrders, None, "buy ticker should be matched and thus gone")
        self.assertEqual(orderBook.sellOrders, None, "sell ticker should be matched and thus gone")


    def test_one_sell_left_match(self):
        orderBook = OrderBook()
        OrderBook.addOrder(orderBook, "BUY", "ticker1", 110, 50.0)
        OrderBook.addOrder(orderBook, "SELL", "ticker1", 150, 20.0)

        OrderBook.matchOrder(orderBook, "ticker1")

        self.assertEqual(orderBook.buyOrders, None, "buy ticker should be matched and thus gone")

        self.assertEqual(orderBook.sellOrders.OrderType, "SELL", 'sell order after match. (ordertype)')
        self.assertEqual(orderBook.sellOrders.TickerSymbol, "ticker1", 'sell order after match. (tickersymbol)')
        self.assertEqual(orderBook.sellOrders.Qty, 40, 'sell order after match. (quantity)')
        self.assertEqual(orderBook.sellOrders.Price, 20.0, 'sell order after match. (price)')


    def test_one_buy_left_match(self):
        orderBook = OrderBook()
        OrderBook.addOrder(orderBook, "BUY", "ticker1", 150, 50.0)
        OrderBook.addOrder(orderBook, "SELL", "ticker1", 110, 20.0)

        OrderBook.matchOrder(orderBook, "ticker1")

        self.assertEqual(orderBook.sellOrders, None, "sell ticker should be matched and thus gone")

        self.assertEqual(orderBook.buyOrders.OrderType, "BUY", 'the first buy order insert wrongly. (ordertype)')
        self.assertEqual(orderBook.buyOrders.TickerSymbol, "ticker1", 'the first s order insert wrongly. (tickersymbol)')
        self.assertEqual(orderBook.buyOrders.Qty, 40, 'the first buy order insert wrongly. (quantity)')
        self.assertEqual(orderBook.buyOrders.Price, 50.0, 'the first buy order insert wrongly. (price)')

    # def test_update_buy_head(self):
    #     orderBook = OrderBook()
    #     OrderBook.addOrder(orderBook, "BUY", "ticker1", 110, 50.0)
    #     OrderBook.addOrder(orderBook, "SELL", "ticker1", 150, 20.0)
    #     OrderBook.addOrder(orderBook, "BUY", "ticker2", 30, 20.0)

    #     OrderBook.matchOrder(orderBook, "ticker1")

    #     self.assertEqual(orderBook.sellOrders, None, "sell ticker should be matched and thus gone")

    #     self.assertEqual(orderBook.buyOrders.OrderType, "BUY", 'the first buy order insert wrongly. (ordertype)')
    #     self.assertEqual(orderBook.buyOrders.TickerSymbol, "ticker2", 'the first s order insert wrongly. (tickersymbol)')
    #     self.assertEqual(orderBook.buyOrders.Qty, 30, 'the first buy order insert wrongly. (quantity)')
    #     self.assertEqual(orderBook.buyOrders.Price, 20.0, 'the first buy order insert wrongly. (price)')

    #     self.assertEqual(orderBook.sellOrders.OrderType, "SELL", 'sell order after match. (ordertype)')
    #     self.assertEqual(orderBook.sellOrders.TickerSymbol, "ticker1", 'sell order after match. (tickersymbol)')
    #     self.assertEqual(orderBook.sellOrders.Qty, 40, 'sell order after match. (quantity)')
    #     self.assertEqual(orderBook.sellOrders.Price, 20.0, 'sell order after match. (price)')

    # def test_update_sell_head(self):
    #     orderBook = OrderBook()
    #     OrderBook.addOrder(orderBook, "BUY", "ticker1", 150, 50.0)
    #     OrderBook.addOrder(orderBook, "SELL", "ticker1", 110, 20.0)
    #     OrderBook.addOrder(orderBook, "SELL", "ticker2", 30, 20.0)

    #     OrderBook.matchOrder(orderBook, "ticker1")

    #     self.assertEqual(orderBook.sellOrders, None, "sell ticker should be matched and thus gone")

    #     self.assertEqual(orderBook.buyOrders.OrderType, "BUY", 'the first buy order insert wrongly. (ordertype)')
    #     self.assertEqual(orderBook.buyOrders.TickerSymbol, "ticker1", 'the first s order insert wrongly. (tickersymbol)')
    #     self.assertEqual(orderBook.buyOrders.Qty, 40, 'the first buy order insert wrongly. (quantity)')
    #     self.assertEqual(orderBook.buyOrders.Price, 50.0, 'the first buy order insert wrongly. (price)')

    #     self.assertEqual(orderBook.sellOrders.OrderType, "SELL", 'sell order after match. (ordertype)')
    #     self.assertEqual(orderBook.sellOrders.TickerSymbol, "ticker2", 'sell order after match. (tickersymbol)')
    #     self.assertEqual(orderBook.sellOrders.Qty, 30, 'sell order after match. (quantity)')
    #     self.assertEqual(orderBook.sellOrders.Price, 20.0, 'sell order after match. (price)')

    
    # def test_one_buy_two_sell_match(self):
    #     orderBook = OrderBook()
    #     OrderBook.addOrder(orderBook, "BUY", "ticker1", 150, 50.0)
    #     OrderBook.addOrder(orderBook, "SELL", "ticker1", 110, 20.0)
    #     OrderBook.addOrder(orderBook, "SELL", "ticker1", 30, 20.0)

    #     OrderBook.matchOrder(orderBook, "ticker1")

    #     self.assertEqual(orderBook.sellOrders, None, "sell ticker should be matched and thus gone")

    #     self.assertEqual(orderBook.buyOrders.OrderType, "BUY", 'the first buy order insert wrongly. (ordertype)')
    #     self.assertEqual(orderBook.buyOrders.TickerSymbol, "ticker1", 'the first s order insert wrongly. (tickersymbol)')
    #     self.assertEqual(orderBook.buyOrders.Qty, 10, 'the first buy order insert wrongly. (quantity)')
    #     self.assertEqual(orderBook.buyOrders.Price, 50.0, 'the first buy order insert wrongly. (price)')

if __name__ == '__main__':
    unittest.main()
