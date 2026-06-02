def sequence_potential(hand):
    """
    Estimate number of potential sequences in a hand
    """
    from itertools import combinations
    potential = 0
    # all 3cards
    for combo in combinations(hand, 3):
        ranks = [c[:-1] for c in combo]
        if len(set(ranks)) == 3: 
            potential +=1
    return potential


if __name__ == "__main__":
    hand = ['7H','8H','9H','KS','KD','KC']
    print("Sequence Potential:", sequence_potential(hand))
