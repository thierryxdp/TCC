def uppCons(x):
    i=0
    while i<len(x):
        if x[i] not in 'AEIOUaeiou':
            x[i].upper
        i+=1
    return x