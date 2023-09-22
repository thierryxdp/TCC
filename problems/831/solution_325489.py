def lingua_p(palavra):
    """retorna a frase de entrada com todas suas consoantes maiusculas """
    saida = []
    palavraP = []
    for i in palavra:
        palavraP += i
        if i in "AEIOUaeiouÃãÁáÀàÉéÍíÕõÓóÚú":
        """   strA = "".join('p')
         palavraP += strA"""
         palavraP += "".join('p')
            palavraP += i
            saida = "".join(palavraP)
        else:
            saida += i
        
    return saida