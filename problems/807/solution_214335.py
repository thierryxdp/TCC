def conta_frases(texto):
    '''Função que retorna o número de frases de um texto. Considera que as frases terminam
    com '.','!','?' e '...' e as pontuações não devem estar repetidas no texto.
    Entrada: srt. Saída: int.'''
    r = str.count(texto,'...')
    p = str.count(texto,'.')
    e = str.count(texto,'!')
    i = str.count(texto,'?')
    if r!=p
    return p + e + i + r