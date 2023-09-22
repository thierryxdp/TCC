def uppCons(frase):
    for e in frase:
        if e not in ["AEIOUaeiou"]:
            M = str.upper(e)
    return M