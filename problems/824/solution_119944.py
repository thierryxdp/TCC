def uppCons(x):
    i=0
    while i<len(x):
        if x[i] in not ["a","e","i","o","u"]:
            x.upper(x[i])
            
    return x