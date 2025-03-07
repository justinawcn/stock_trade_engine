from enum import Enum
from typing import Union

class Order:
    def __init__(self, OrderType, TickerSymbol, Qty, Price):
        self.OrderType = OrderType
        self.TickerSymbol = TickerSymbol
        self.Qty = Qty
        self.Price = Price
        self.prev = None
        self.next = None



class OrderType(Enum):
    BUY = True
    SELL = False



class TickerType:
    def __init__(self, symbol: Union[int, str]):
        if isinstance(symbol, int):
            if not (0 <= symbol < 1024):
                raise ValueError("Integer ticker symbols outside the bound, 0 - 1023")
        elif not isinstance(symbol, str):
            raise TypeError("Ticker symbol isn't an integer or a string which is incorrect")
        self.symbol = symbol

    def __str__(self):
        return str(self.symbol)




class OrderBook():
    BUY = 0
    SELL = 1


    def __init__(self):
        self.buyOrders = None # descending order
        self.sellOrders = None # ascending order


    def addOrder(self, orderType: str, tickerSymbol: TickerType, qty: int, price: float):
        added_order = Order(orderType, tickerSymbol, qty, price)

        if orderType == "BUY":
            if self.buyOrders is None:
                self.buyOrders = added_order
            else:
                # traversing the buy list and store in a descending order

                # adding to the head 
                if added_order.Price > self.buyOrders.Price:
                    self.buyOrders.prev = added_order
                    added_order.next = self.buyOrders
                    self.buyOrders = added_order
                    return
                
                ptr = self.buyOrders
                previous_order = self.buyOrders
                while (ptr.Price > added_order.Price):
                    if ptr.next is None:
                        break
                    previous_order = ptr
                    ptr = ptr.next
                # current order price is no longer greater than the order to be added
                # the order should be added before the current order
                previous_order.next = added_order
                added_order.next = ptr
                ptr.prev = added_order
        elif orderType == "SELL":
            if self.sellOrders is None:
                self.sellOrders = added_order
            else:
                # traversing the sell list and store in a ascending order

                # adding to the head
                if added_order.Price < self.sellOrders.Price:
                    self.sellOrders.prev = added_order
                    added_order.next = self.sellOrders
                    self.sellOrders = added_order
                    return 
                
                ptr = self.sellOrders
                previous_order = self.sellOrders
                while (ptr.Price < added_order.Price):
                    if ptr.next is None:
                        break
                    previous_order = ptr
                    ptr = ptr.next
                previous_order.next = added_order
                added_order.next = ptr
                ptr.prev = added_order
        else:
            raise ValueError("incorrect orderType, neither BUY nor SELL")


    # def matchOrder(self, tickerSymbol):

        # O(n)



# def stimulator() {

# }

if __name__ == '__main__':
    print("market starts...")
    stockMarket = OrderBook()
