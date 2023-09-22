def separacao(x):
    v = []
    j = str.split(x)
    for p in j:
        for l in len(p):
            v = v + l
    return v
def uppCons (f):
    return separacao(f)