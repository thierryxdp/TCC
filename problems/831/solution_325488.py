def lingua_p(palavra):
    """retorna a frase de entrada com todas suas consoantes maiusculas """
    saida = []
    palavraP = []
    for i in palavra:
        palavraP += i
        if i in "AEIOUaeiouÃãÁáÀàÉéÍíÕõÓóÚú":
            palavraP = "".join('p')
            palavraP += palavraP
            palavraP += i
            saida = "".join(palavraP)
        else:
            saida += i
        
    return saida