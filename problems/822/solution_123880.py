from collections import defaultdict
def repetidos(num):
    repet = defaultdict(list);
    for key, value in enumerate(num):
        repet[value].append(key)
    return value