def uppCons(x):
    c=0
    f=""
    while c<len(x):
        if x[c] in ('A','E','I','O','U','a','e','i','o','u'):
        f.append(x[c])
    return f