import Row_Class
import Column_Class
import Square_Class

class Field:
    def __init__(self, row : Row_Class.Row, column : Column_Class.Column, square : Square_Class.Square):
        self.candidates = set(i for i in range(1,10))