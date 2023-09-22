def uppCons(frase):
    """ """
    saida = ""
    for i in frase:
        if (i in "AEIOUaeiou"):
            saida += i
        else:
            s = ""
            s = str(i)
            s.uuper()
            saida += i
    return