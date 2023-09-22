def lingua_p(palavra):
    """retorna a palara recebida, sendo apos cada vogal da palavra original, insere a letra p mais a vogal original"""
    saida = []
    palavraP = []
    for i in palavra:
        palavraP += i
        if i in "AEIOUaeiouÃãÁáÀàÉéÍíÕõÓóÚú":
            palavraP += "".join('p')
            palavraP += i
            saida = "".join(palavraP)
        else:
            saida += i
        
    return saida