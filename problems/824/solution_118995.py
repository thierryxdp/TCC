def uppCons(frase):
    fn = " "
    for e in frase:
        if e not in ["AEIOUaeiou"]:
            M = str.upper(e)
            fn = fn + M
        else:
            N = str.lower(e)
            fn = fn + N
    return fn