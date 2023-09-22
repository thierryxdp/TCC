from collections import defaultdict
def repetidos(num):
    repet = defaultdict(list);
    for key, value in enumerate(num):
        keys[value].append(key)
    for value in keys:
        if len(keys[value]) > 1:
            print(value, keys[value])