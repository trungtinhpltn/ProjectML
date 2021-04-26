import pandas as pd
import numpy as np
from utils import *
from collections import defaultdict
from itertools import permutations
from optparse import OptionParser
from mlxtend.preprocessing import TransactionEncoder

path_to_data= "BTL/Data/groceries - groceries.csv"
transactions= load_transactions(path_to_data)

# def apriori(transactions, minSup, minConf):
#     C1ItemSet = preprocessing(transactions);
#     globalFreqItemSet = dict()
#     globalItemSetWithSup = defaultdict(int)

#     L1ItemSet = getAboveMinSup( C1ItemSet, transactions, minSup, globalItemSetWithSup)
#     currentLSet = L1ItemSet
#     k = 2

#     while(currentLSet):
#         globalFreqItemSet[k-1] = currentLSet
#         candidateSet = getUnion(currentLSet, k)
#         candidateSet = pruning(candidateSet, currentLSet, k-1)
#         currentLSet = getAboveMinSup(
#             candidateSet, transactions, minSup, globalItemSetWithSup)
#         k += 1

#     rules = associationRule(globalFreqItemSet, globalItemSetWithSup, minConf)
#     rules.sort(key=lambda x: x[2])

#     return globalFreqItemSet, rules

# freqItemSet, rules = apriori(transactions, 0.03, 0.05)
C1ItemSet= preprocessing(transactions)
print (C1ItemSet['pip fruit'])