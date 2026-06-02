from itertools import groupby

class RummyHandAnalyzer:

    def __init__(self, hand):
        self.hand = hand

    def pure_sequences(self):
        sequences = []
        hand_by_suit = {}
        for card in self.hand:
            rank, suit = card[:-1], card[-1]
            hand_by_suit.setdefault(suit, []).append(rank)

        for suit, ranks in hand_by_suit.items():
            # translate to num，A=1, J=11, Q=12, K=13
            rank_map = {'A':1,'J':11,'Q':12,'K':13}
            nums = [rank_map.get(r,int(r)) for r in ranks]
            nums.sort()
            seq_count = 0
            for i in range(len(nums)-2):
                if nums[i+1] == nums[i]+1 and nums[i+2] == nums[i]+2:
                    seq_count +=1
            sequences.append(seq_count)
        return sum(sequences)

    def sets(self):
        rank_count = {}
        for card in self.hand:
            rank = card[:-1]
            rank_count[rank] = rank_count.get(rank,0)+1
        return sum(1 for count in rank_count.values() if count>=3)

    def dead_cards(self):
        return len(self.hand) - self.pure_sequences()*3 - self.sets()*3


if __name__ == "__main__":
    hand = ['7H','8H','9H','KS','KD','KC','2D']
    analyzer = RummyHandAnalyzer(hand)
    print("Pure sequences:", analyzer.pure_sequences())
    print("Sets:", analyzer.sets())
    print("Dead cards:", analyzer.dead_cards())
