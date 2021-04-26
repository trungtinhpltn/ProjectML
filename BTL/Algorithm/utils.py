import pandas as pd
import numpy as np
from itertools import permutations
from collections import defaultdict
from mlxtend.preprocessing import TransactionEncoder

def load_transactions(path_to_data):
    groceries = pd.read_csv(path_to_data, encoding ="utf-8")
    groceries.head()
    trans_df = groceries
    del trans_df['Item(s)']
    trans_df.fillna(0,inplace=True)
    transactions = []
    for i in range(0, len(trans_df)):
        transactions.append([str(trans_df.values[i,j]) for j in range(0, 31) if str(trans_df.values[i,j])!='0'])
    return transactions

def preprocessing(transactions):
    C1ItemSet= set()
    encoder = TransactionEncoder().fit(transactions)
    onehot = encoder.transform(transactions)
    onehot = pd.DataFrame(onehot, columns = encoder.columns_)
    support= onehot.mean();
    C1ItemSet= set(support)

    flattened = [i for t in transactions for i in t]
    groceries = list(set(flattened))

    # Generate all possible rules
    rules = list(permutations(groceries, 2))
    return C1ItemSet



def getAboveMinSup(itemSet, itemSetList, minSup, globalItemSetWithSup):
    freqItemSet = set()
    localItemSetWithSup = defaultdict(int)

    for item in itemSet:
        for itemSet in itemSetList:
            if item.issubset(itemSet):
                globalItemSetWithSup[item] += 1
                localItemSetWithSup[item] += 1

    for item, supCount in localItemSetWithSup.items():
        support = float(supCount / len(itemSetList))
        if(support >= minSup):
            freqItemSet.add(item)

    return freqItemSet

def getUnion(itemSet, length):
    return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])

def pruning(candidateSet, prevFreqSet, length):
    tempCandidateSet = candidateSet.copy()
    for item in candidateSet:
        subsets = combinations(item, length)
        for subset in subsets:
            if(frozenset(subset) not in prevFreqSet):
                tempCandidateSet.remove(item)
                break
    return tempCandidateSet

def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)))

def associationRule(freqItemSet, itemSetWithSup, minConf):
    rules = []
    for k, itemSet in freqItemSet.items():
        for item in itemSet:
            subsets = powerset(item)
            for s in subsets:
                confidence = float(
                    itemSetWithSup[item] / itemSetWithSup[frozenset(s)])
                if(confidence > minConf):
                    rules.append([set(s), set(item.difference(s)), confidence])
    return rules
