def uppCons(x):
    i = 0
    f = ''
    while i < len(x):
        if x[i] not in 'aeiouAEIOU':
            f += x[i]
        i += 1
    return x