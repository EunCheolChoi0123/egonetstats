import pandas as pd
import numpy as np
from scipy.stats import mode
from collections import Counter

def blau_index(values):
    counts = Counter(values)
    total = sum(counts.values())
    if total == 0:
        return np.nan
    proportions = [v / total for v in counts.values()]
    return 1 - sum(p ** 2 for p in proportions)

def iqv(values):
    counts = Counter(values)
    total = sum(counts.values())
    k = len(counts)
    if total == 0:
        return np.nan
    if k == 1:
        return 0.0  # Edge case; no variation
    p_squared_sum = sum((count / total) ** 2 for count in counts.values())
    return (k / (k - 1)) * (1 - p_squared_sum)

def egonet_composition(df, column_list, stat, category=None):
    results = []

    for _, row in df.iterrows():
        values = row[column_list].dropna()

        if len(values) == 0:
            results.append(np.nan)
            continue

        try:
            if stat == 'count':
                results.append(len(values))
            elif stat == 'mean':
                results.append(np.mean(values.astype(float)))
            elif stat == 'median':
                results.append(np.median(values.astype(float)))
            elif stat == 'mode':
                results.append(mode(values)[0][0])
            elif stat == 'std':
                results.append(np.std(values.astype(float), ddof=1))
            elif stat == 'blau':
                results.append(blau_index(values))
            elif stat == 'iqv':
                results.append(iqv(values))
            elif stat == 'proportion' and category is not None:
                values = values.astype(str)
                count_cat = sum(values == category)
                results.append(count_cat / len(values))
            else:
                results.append(np.nan)
        except:
            results.append(np.nan)

    return results
