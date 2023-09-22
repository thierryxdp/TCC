from collections import defaultdict
def repetidos(num):
    repet = defaultdict(list);
    for key, value in enumerate(num):
        repet[value].append(key)
    for value in repet:
        if len(keys[value]) > 1:
            print(value, keys[value])