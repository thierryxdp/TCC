def uppCons(frase):
    """ """
    frase1 = ""
    for i in frase:
        if (i in "AEIOUaeiou"):
            frase1 += i
        else:
            frase1.upper(1)
    return frase1