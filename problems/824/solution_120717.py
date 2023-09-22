def uppCons(x):
    n = 0
    while n<len(x):
        if x[n] != 'a' and 'e' and 'i' and 'o' and 'u':
            x[n].upper()
        n=n+1
    return x