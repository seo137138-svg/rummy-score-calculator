# Rummy Hand Analysis Toolkit

An open-source Python toolkit for analyzing Indian Rummy hands, calculating scores, evaluating potential sequences and sets, and estimating bonus wagering requirements.

---

## Features

- **Hand Score Calculation** – Computes dead card points using standard Indian Rummy rules.
- **Hand Analyzer** – Detects pure sequences, sets, and dead cards in a hand.
- **Bonus Requirement Calculator** – Estimates total play volume required to unlock bonus offers.
- **Probability Engine** – Estimates potential sequences for strategy analysis.

---

## Quick Start

```python
from score_calculator import ScoreCalculator
from hand_analyzer import RummyHandAnalyzer
from bonus_calculator import calculate_bonus_requirement

hand = ['7H','8H','9H','KS','KD','KC']
analyzer = RummyHandAnalyzer(hand)

print("Pure sequences:", analyzer.pure_sequences())
print("Sets:", analyzer.sets())
print("Dead cards:", analyzer.dead_cards())

required_play = calculate_bonus_requirement(500, 100, 5)
print("Required play volume for bonus:", required_play)
