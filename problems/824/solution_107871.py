def uppCons(frase):
    """ """
    saida = ""
    for i in frase:
        if (i in "AEIOUaeiou"):
            saida += i
        else:
            i.upper()
            saida += i
    return i