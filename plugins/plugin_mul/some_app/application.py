
class Operation:
    def __init__(self, a=100, b=50) -> None:
        self.a = a
        self.b = b

    def get(self):
        return f"Multiplication is {self.a * self.b}"
