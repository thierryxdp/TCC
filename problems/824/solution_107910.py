def uppCons(frase):
    """retorna a frase de entrada com todas suas consoantes maiusculas """
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