def uppCons(frase):
    """ """
    saida = []
    saida2 = ""
    for i in frase:
        if (i in "AEIOUaeiou"):
            saida += i
        else:
            s = ""
            s = i
            s.upper()
            saida += s
            saida2.join(saida)
    return saida