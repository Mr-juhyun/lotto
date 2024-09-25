import pandas as pd
lotto1 = pd.read_excel('./first.xlsx')
lotto2 = pd.read_excel('./sec.xlsx')
lotto1.columns =['n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'bonus']
lotto = pd.concat([lotto1,lotto2],ignore_index=True)
lotto.to_csv('./lotto_data')
