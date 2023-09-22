def uppCons(frase):
    """ """
    frase1 = str()
    for i in frase:
        if (i in "AEIOUaeiou"):
            frase1.append(i)
        else:
            frase1.append(i.upper())
    return frase1