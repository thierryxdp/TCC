def uppCons(x):
    i=0
    while i<len(x):
        if x[i] in 'aeiou':
            str.upper(x[i])
        i+=1
    return x