# The number of dogs given and sorted within a data set

animals = {'dogs': [20, 10, 15, 8, 32, 15],
           'cats': [3,4,2,8,2,4],
           'rabbits': [2, 3, 3],
           'fish': [0.3, 0.5, 0.8, 0.3, 1]}

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H', 'is_noble_gas': "False"},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He','is_noble_gas': "True"}}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't
elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True
