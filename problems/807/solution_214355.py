def conta_frases(texto):
    '''Função que retorna o número de frases de um texto. Considera que as frases terminam
    com '.','!','?' e '...'. As pontuações não devem estar repetidas no texto.
    Entrada: srt. Saída: int.'''
    r = str.count(texto,'...')
    p = str.count(texto,'.')
    e = str.count(texto,'!')
    i = str.count(texto,'?')
    if '...' in texto:
        return (p + e + i + r)-(3*r)
    else:
        return p + e + i + r