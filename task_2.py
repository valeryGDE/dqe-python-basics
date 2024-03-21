import random
import string
from collections import defaultdict


def generate_single_dict():
    return {random.choice(string.ascii_lowercase): random.randint(0, 100) for _ in range(random.randint(3, 4))}


def generate_dicts(a, b):
    return [generate_single_dict() for _ in range(random.randint(a, b))]


dict_list = generate_dicts(2, 11)

print(dict_list)


def count_keys(dicts):
    key_count = defaultdict(int)
    for d in dicts:
        for k in d.keys():
            key_count[k] += 1
    return key_count


def find_common_dict(dicts):
    common_dict = defaultdict(int)
    dict_number = defaultdict(str)

    for i, d in enumerate(dicts, 1):
        for k, v in d.items():
            if v > common_dict[k]:
                common_dict[k] = v
                dict_number[k] = str(i)

    return common_dict, dict_number


def rename_keys(common_dict, dict_number, key_count):
    renamed_dict = {
        k + ('_' + dict_number[k] if key_count[k] > 1 else ''): v
        for k, v in common_dict.items()
    }
    return renamed_dict


def process_dicts(dicts):
    key_count = count_keys(dicts)
    common_dict, dict_number = find_common_dict(dicts)
    renamed_dict = rename_keys(common_dict, dict_number, key_count)
    return renamed_dict


print(process_dicts(dict_list))
