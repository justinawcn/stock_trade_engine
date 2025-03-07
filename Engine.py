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
                    return self.matchOrder(added_order.TickerSymbol)
                
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
                return self.matchOrder(added_order.TickerSymbol)
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
                    return self.matchOrder(added_order.TickerSymbol)
                
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
                return self.matchOrder(added_order.TickerSymbol)
        else:
            raise ValueError("incorrect orderType, neither BUY nor SELL")


    def matchOrder(self, tickerSymbol):
        # O(n)
        buy = self.buyOrders
        sell = self.sellOrders
        while buy is not None and sell is not None:
            if buy.TickerSymbol != tickerSymbol:
                buy = buy.next
                continue
            if sell.TickerSymbol != tickerSymbol:
                sell = sell.next
                continue

            if buy.Price >= sell.Price:
                matched_qty = min(buy.Qty, sell.Qty)

                buy.Qty -= matched_qty
                sell.Qty -= matched_qty

                if buy.Qty == 0:
                    self._remove_order(OrderType.BUY, buy)
                    if buy is not None:
                        buy = buy.next

                if sell.Qty == 0:
                    print("sell empty")
                    self._remove_order(OrderType.SELL, sell)
                    if sell is not None:
                        sell = sell.next
                
            else:
                break

    def _remove_order(self, OrderType, order):
        """helper function to remove an order from the linked list"""
        if OrderType:
            if self.buyOrders == order:
                if order is not None:
                    self.buyOrders = order.next
                else:
                    self.buyOrders = None
            else:
                if order is not None:
                    order.prev.next = order.next
                    order.next.prev = order.prev
                else:
                    order.prev.next = None
        else:
            if self.sellOrders == order:
                if order is not None:
                    self.sellOrders = order.next
                else:
                    self.sellOrders = None
            else:
                if order is not None:
                    order.prev.next = order.next
                    order.next.prev = order.prev
                else:
                    order.prev.next = None





# def stimulator() {

# }

if __name__ == '__main__':
    print("market starts...")
    stockMarket = OrderBook()
