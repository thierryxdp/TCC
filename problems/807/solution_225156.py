def conta_frases(frase):
    """"""
    pRet = str.count(frase, '...')
    pFinal = str.count(frase, '.')
    pExc = str.count(frase, '!')
    pInt = str.count(frase, '?')
    total_frases = pFinal + pExc + pInt + pRet
    return total_frases