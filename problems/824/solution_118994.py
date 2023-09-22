def uppCons(frase):
    fn = " "
    for e in frase:
        if e not in ["AEIOUaeiou"]:
            M = str.upper(e)
            fn = fn + M
    return fn