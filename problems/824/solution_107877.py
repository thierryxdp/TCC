def uppCons(frase):
    """ """
    saida = []
    for i in frase:
        if (i in "AEIOUaeiou"):
            saida += i
        else:
            s = ""
            s = i
            s.upper()
            saida += s
    return saida