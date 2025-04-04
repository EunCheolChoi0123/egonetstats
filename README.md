# egonetstats

This small package provides functions for calculating egonet composition statistics, including Blau's Index, IQV, and category proportions across alter attributes.

## Installation
```
pip install git+https://github.com/EunCheolChoi0123/egonetstats.git
```

Alternatively, clone the repo and install it locally:

```
pip install -e .
```

## Usage

```python
from egonetstats import egonet_composition, blau_index, iqv
```

## Example Code
```
import pandas as pd
import numpy as np

data = {
    'participant_id': [13534091,146317502,13532533,1358974364,3150838405],
    'f1_name': ['A', 'B', 'C', 'D', np.nan],
    'f2_name': ['B', 'E', 'F', 'D', 'G'],
    'f3_name': ['E', 'C', np.nan, 'D', 'H'],
    'f1_gender': ['M', 'F', 'F', 'M', np.nan],
    'f2_gender': ['F', 'F', 'M', 'M', 'F'],
    'f3_gender': ['F', 'M', np.nan, 'M', 'F'],
    'f1_age': [25, 30, 22, 28, np.nan],
    'f2_age': [26, 31, 24, 29, 27],
    'f3_age': [27, 29, np.nan, 27, 28],
}

df = pd.DataFrame(data)

df['network_size'] = egonet_composition(df, ['f1_name', 'f2_name', 'f3_name'], stat='count')

# For continuous variables
df['age_mean'] = egonet_composition(df, ['f1_age', 'f2_age', 'f3_age'], stat='mean')
df['age_std'] = egonet_composition(df, ['f1_age', 'f2_age', 'f3_age'], stat='std')
df['age_median'] = egonet_composition(df, ['f1_age', 'f2_age', 'f3_age'], stat='median')

# For categorical variables
df['female_prop'] = egonet_composition(df, ['f1_gender', 'f2_gender', 'f3_gender'], stat='proportion', category='F') # Proportion of alters belonging in a certain category.
df['gender_blau'] = egonet_composition(df, ['f1_gender', 'f2_gender', 'f3_gender'], stat='blau')                     # Blau's index: A measure of observed diversity.
df['gender_iqv'] = egonet_composition(df, ['f1_gender', 'f2_gender', 'f3_gender'], stat='iqv')                       # IQV: An another measure of observed diversity. Basically a normalized version of Blau's index. Defaults to 0 when there is only one observed category.
```

## Future work
- Implement pipeline calculating structural properties, utilizing alter-alter ties.
- Add other compositional measures (open to suggestions)
