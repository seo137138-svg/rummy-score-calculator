from itertools import combinations

def sequence_potential(hand):
    potential = 0
    for combo in combinations(hand, 3):
        ranks = [c[:-1] for c in combo]
        if len(set(ranks)) == 3:
            potential +=1
    return potential

if __name__ == "__main__":
    hand = ['7H','8H','9H','KS','KD','KC']
    print("Sequence Potential:", sequence_potential(hand))
