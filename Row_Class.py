class Row:
    def __init__(self, x : int):
        self.candidates = set(i for i in range(1,10))
        self.x = x
        