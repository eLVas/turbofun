

import pandas as pd

from matplotlib import pyplot
col_names = ['un', 'cycles', 'op_s_1', 'op_s_2', 'op_s_3'] + [ 'sens_val_' + str(x) for x in range(1,22)]

df = pd.read_csv('data/CMAPSSData/train_FD001.txt',
                 index_col=False,
                 header=None,
                 delimiter=' ',
                 names=col_names,
                 usecols=col_names)
