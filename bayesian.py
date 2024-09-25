import pandas as pd
from collections import defaultdict
class Bayesian:
    def __init__(self,lotto):
        self.lotto = lotto
        self.top_numbers = []
    def bay(self):
        numbers = range(1, 46)
        number_counts = defaultdict(int)

        for index, row in self.lotto.iterrows():
            for number in row:
                number_counts[number] += 1

        total_draws = len(self.lotto)

        prior_prob = 1 / len(numbers)

        bayesian_probs = {}
        for number in numbers:
            likelihood = number_counts[number] / total_draws
            
            bayesian_probs[number] = likelihood * prior_prob

        self.top_numbers = sorted(bayesian_probs, key=bayesian_probs.get, reverse=True)[:6]

