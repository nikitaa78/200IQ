class Card:
	def __init__(self, suit, val):
		self.suit = suit
		self.value = val

class Deck:
	def __init__(self):
		self.cards = []
		self.build()

	def build(self):
		for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
			for v in range(1, 14):
				self.cards.append(Card(s, v))


class Game:
	def __init__(self, deck, players):
		self.deck = Deck().cards

	def deal(self, players, cards):
		#assign equal number cards to players randomly


