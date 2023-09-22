from collections import defaultdict
def repetidos(nums):
    rep = defaultdict(list);
    for key, value in enumerate(num):
        rep[value].append(key)
        for value in keys:
    if len(rep[value]) > 1:
        print(value, rep[value])