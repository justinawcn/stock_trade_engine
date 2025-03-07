from enum import enum

class Order:
    def __init__(self, OrderType, TickerSymbol, Qty, Price):
        self.OrderType = OrderType
        self.TickerSymbol = TickerSymbol
        self.Qty = Qty
        self.Price = Price
        self.prev = None
        self.next = None



class OrderType(enum):
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


    def addOrder(self, orderType: String, tickerSymbol: TickerType, qty: Int, price: Float) {
        added_order = Order(orderType, tickerSymbol, qty, price)

        if orderType == "BUY":
            
            if self.buyOrders is None:
                self.buyOrders = added_order
            else:
                # traversing the buy list and store in a descending order
                ptr = self.buyOrders
                while (ptr.price > added_order.price):
                    previous_order = ptr
                    ptr = ptr.next
                # current order price is no longer greater than the order to be added
                # the order should be added before the current order
                previous_order.next = added_order
                added_order.next = ptr
                ptr.prev = added_order

    }

    def matchOrder(self, TickerSymbol) { 
        # O(n)

    }

def stimulator() {

}

def main() {
    print("market starts...")
    stockMarket = new OrderBook
}
