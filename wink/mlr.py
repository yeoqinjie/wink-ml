from sklearn import tree
import numpy as np

features = ((0, 0), (0, 0), (1, 1), (1, 1)) # 0 = smooth
results = (90, 110, 140, 160) # 0 = apple

machine = tree.DecisionTreeClassifier()
machine.fit(features, results)

print machine.predict((1, 1))