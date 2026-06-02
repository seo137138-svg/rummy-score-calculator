class ScoreCalculator:
    CARD_VALUES = {
        'A': 10, 'J': 10, 'Q': 10, 'K': 10
    }

    def __init__(self, jokers=[]):
        self.jokers = jokers  # list of joker cards

    def card_value(self, card):
        rank = card[:-1]  # strip suit
        if rank in self.jokers:
            return 0
        return self.CARD_VALUES.get(rank, int(rank))

    def calculate_score(self, hand):
        return sum(self.card_value(card) for card in hand)


if __name__ == "__main__":
    hand = ['A♠', '7♥', 'Q♦', '5♣', 'JOKER']
    calculator = ScoreCalculator(jokers=['JOKER'])
    print("Hand Score:", calculator.calculate_score(hand))
