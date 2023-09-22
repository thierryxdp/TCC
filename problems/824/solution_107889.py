def uppCons(frase):
    """ """
    saida = []
    for i in frase:
        if (i in "AEIOUaeiouÃã"):
            saida += i
        else:
            s = ""
            s = i.upper()
           
            saida += s
            strA = "".join(saida)
    return strA