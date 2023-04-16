import pandas as pd

# dataset 1
cols1 = ['SHORT-LINE-DENSITY-5',  'SHORT-LINE-DENSITY-2', 'VEDGE-MEAN', 'VEDGE-SD', 'HEDGE-MEAN', 'HEDGE-SD']
train1 = pd.read_csv('segmentation.data', header=2, usecols=cols1)
test1 = pd.read_csv('segmentation.test', header=2, usecols=cols1)
data1 = pd.concat([train1, test1])

# dataset 2
cols2 = ['INTENSITY-MEAN','RAWRED-MEAN','RAWBLUE-MEAN','RAWGREEN-MEAN','EXRED-MEAN','EXBLUE-MEAN','EXGREEN-MEAN','VALUE-MEAN','SATURATION-MEAN','HUE-MEAN']
train2 = pd.read_csv('segmentation.data', header=2, usecols=cols2)
test2 = pd.read_csv('segmentation.test', header=2, usecols=cols2)
data2 = pd.concat([train2, test2])

# dataset 3
cols3 = cols1 + cols2
train3 = pd.read_csv('segmentation.data', header=2, usecols=cols3)
test3 = pd.read_csv('segmentation.test', header=2, usecols=cols3)
data3 = pd.concat([train3, test3])
