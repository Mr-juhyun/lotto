from bayesian import Bayesian
from markov_chain import MarkovChain
import pandas as pd


lotto = pd.read_csv('./lotto_data')
lotto.drop(columns='Unnamed: 0',inplace=True)


bay = Bayesian(lotto)
bay.bay()
print(sorted(bay.top_numbers))
mark = MarkovChain(lotto)
mark.markov()
print(sorted(mark.pred))