def calculate_bonus_requirement(deposit, bonus_percent, wager_multiplier):
    bonus_amount = deposit * bonus_percent / 100
    total_play = (deposit + bonus_amount) * wager_multiplier
    return total_play

if __name__ == "__main__":
    deposit = 500
    bonus_percent = 100
    wager_multiplier = 5
    print("Required Play Volume:", calculate_bonus_requirement(deposit, bonus_percent, wager_multiplier))
