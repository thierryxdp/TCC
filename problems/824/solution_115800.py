def uppCons(x):
    i = 0
    f = ''
    while i < len(x):
        if not x[i] in 'aeiouAEIOU':
            f = f + str.upper(x[i])
            else: f += x[i]
        i += 1
    return f