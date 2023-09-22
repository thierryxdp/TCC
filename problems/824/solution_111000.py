def uppCons(fra):
    i = 0
    lis = list(fra)
    while i < len(fra):
        if lis[i] not in "AEIOUaeiou":
            lis[i] = str.upper(lis[i])
            i += 1
        else:
            i += 1
    return str.join('', lis)