def conta_frases(text):
    """
    retorna o número de palavras em um texto
    str -> int
    """

    nRet = str.count(text, '...')
    nPontos = str.count(text, '.') - (nRet*3)
    nExcla = str.count(text, '!')
    nInterrog = str.count(text, '?')
    
    return nRet + nPontos + nExcla + nInterrog