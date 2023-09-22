def uppCons(frase):
    """ """
    saida = []
    for i in frase:
        if (i in "AEIOUaeiouÃãÁáÀàÉéÍíÕõÓóÚú"):
            saida += i
        else:
            s = ""
            s = i.upper()
           
            saida += s
            strA = "".join(saida)
    return strA