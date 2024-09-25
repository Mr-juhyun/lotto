import pandas as pd
import numpy as np
from collections import defaultdict

class MarkovChain:
    def __init__(self,lotto):
        self.lotto = lotto
        self.pred = []
    def markov(self,n=6):
        numbers = list(range(1,46))
        tran_matrix = np.zeros((45,45))
        
        for row in self.lotto.values:
            for i in range(len(row)-1):
                cur_num = row[i]
                next_num = row[i+1]
                tran_matrix[cur_num-1][next_num-1] += 1
                
        for i in range(45):
            row_sum = np.sum(tran_matrix[i])
            if row_sum > 0:
                tran_matrix[i] /= row_sum
        
        cur_state = np.random.choice(numbers)
        self.pred = [cur_state]
        
        for _ in range(n-1):
            cur_state_idx = cur_state - 1
            next_state = np.random.choice(numbers,p=tran_matrix[cur_state_idx])
            self.pred.append(next_state)
            cur_state = next_state 