# %%

import pickle

with open('taxicab.pkl', 'rb') as file:
    data = pickle.load(file)

# %%

data[0]
# %%


len(data)
# %%

data[2]
# %%

import numpy as np
[ np.unique(trip) for trip in data ]
# %%


states = set()
for trip in data:
    new_states = set(trip)
    states = states.union(new_states)
# %%
