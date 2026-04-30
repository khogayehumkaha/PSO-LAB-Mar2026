class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price):
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span
    

sp = StockSpanner()
print(sp.next(100))
print(sp.next(80))
print(sp.next(60))
print(sp.next(70))
print(sp.next(60))
print(sp.next(75))
print(sp.next(85))