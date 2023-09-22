from collections import defaultdict
def repetidos(nums):
    rep = defaultdict(list);
    for key, value in enumerate(nums):
        rep[value].append(key)
        for value in rep:
            if len(rep[value]) > 1:
                print(value)