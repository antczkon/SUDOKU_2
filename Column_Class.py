class Column:
    def __init__(self, y : int):
        self.candidates = set(i for i in range(1,10))
        self.y = y