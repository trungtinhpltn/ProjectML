print("HIHI")
print("Hello các bạn")

flattened = [i for t in transactions for i in t]
groceries = list(set(flattened))

# Generate all possible rules
rules = list(permutations(groceries, 1))

# Print the set of rules
print(rules)

# Add a jam+bread column to the DataFrame onehot
onehot['jam+bread'] = np.logical_and(onehot['jam'], onehot['bread'])

# Compute the support
support = onehot.mean()

# Print the support values
print(support)


from mlxtend.frequent_patterns import apriori

# Compute frequent itemsets using the Apriori algorithm
frequent_itemsets = apriori(onehot, 
                            min_support = 0.006, 
                            max_len = 3, 
                            use_colnames = True)

# Print a preview of the frequent itemsets
print(frequent_itemsets.head())


def confidence(antecedent, consequent):
    supportPT= np.logical_and(antecedent, confidence).mean()
    supportP= antecedent.mean()
    return supportPT/ supportP

def lift(antecedent, consequent):
    supportPT = np.logical_and(antecedent, consequent).mean()
    supportP = antecedent.mean()
    supportT = consequent.mean()
    return supportPT / (supportP * supportT)

def conviction(antecedent, consequent):
	supportAC = np.logical_and(antecedent, consequent).mean()
	supportA = antecedent.mean()
	supportnC = 1.0 - consequent.mean()
	supportAnC = supportA - supportAC
	return supportA * supportnC / supportAnC

def zhang(antecedent, consequent):
	supportA = antecedent.mean()
	supportC = consequent.mean()
	numerator = supportAC - supportA*supportC
	denominator = max(supportAC*(1-supportA), supportA*(supportC-supportAC))
	return numerator / denominator

zhangs_metric = []
for itemset in itemsets:
	antecedent = books[itemset[0]]
	consequent = books[itemset[1]]
	zhangs_metric.append(zhang(antecedent, consequent))
rules['zhang'] = zhangs_metric
print(rules)