import random
import string
from collections import defaultdict

# Initialize an empty list to store the dictionaries
dict_list = []

# Generate a random number of dictionaries ranging from 2 to 10 ans loop over this range
for _ in range(random.randint(2, 11)):
    # For each dictionary, generate a random number of keys (either 3 or 4)
    # Create a dictionary with each key as a random letter and each value as a random number from 0 to 100
    new_dict = {random.choice(string.ascii_lowercase): random.randint(0, 100) for _ in range(random.randint(3, 4))}
    # Add the newly created dictionary to the list
    dict_list.append(new_dict)

# Print the list of randomly generated dictionaries
print(dict_list)

# We create a defaultdict called 'common_dict' and set default value as 0 for all new keys
common_dict = defaultdict(int)
# We create another defaultdict called 'dict_number' and set default value as an empty string '' for all new keys
dict_number = defaultdict(str)
# We create another one more defaultdict for storing count of each key
key_count = defaultdict(int)

# Index i starts from 1. Enumerate(dict_list, 1) generates pairs of number-dictionary, starting from 1
for i, d in enumerate(dict_list, 1):
    # For each dictionary (d), go over each key-value pair
    for k, v in d.items():
        # Update the count of current key k in 'key_count'
        key_count[k] += 1
        # If current v is greater than the maximum value for this key
        if v > common_dict[k]:
            # Update max value
            common_dict[k] = v
            # Store current dict number
            dict_number[k] = str(i)

# We create renamed_dict by iterating over the keys and values in common_dict
# If key (k) appears only once in all dictionaries, use key as it is, else append dict number to the key
renamed_dict = {k + ('_' + dict_number[k] if key_count[k] > 1 else ''): v for k, v in common_dict.items()}

# Print the final merged dictionary
print(renamed_dict)
