def uppCons(x): 
    for n in x:
        return str.upper(x)
    for n in x:
        if n in "AEIOUaeiou":
            return str.lower(x)
    return x