from enum import enum

class Order:
    def __init__(self, OrderType, TickerSymbol, Qty, Price):
        self.OrderType = OrderType
        self.TickerSymbol = TickerSymbol
        self.Qty = Qty
        self.Price = Price

class OrderType(enum):
    BUY = True
    SELL = False

class OrderBook():
    def __init__(self):
        self.buyOrders = linkedlist
        self.sellOrders = linkedlist


def addOrder(OrderType: OrderType, TickerSymbol: Type, Qty: Int, Price: Float) {

}

def matchOrder(TickerSymbol) { 
    # O(n)

}

def stimulator() {

}

def main() {
    print("market starts...")
}