# Name: Haydar Hijazi

class Card:
    """class representing a simple Neapolitan card. Holds a 
    value and a suit"""
    def __init__(self,value,suit):
        self.value = int(value)
        self.suit = str(suit)

    def __repr__(self):
        return f"Card(value={self.value},suit ={self.suit})"
    def __str__(self):
        return f"Card({self.value} of {self.suit})"
    def __eq__(self,other):
        return (self.value == other.value, self.suit == other.suit)
      