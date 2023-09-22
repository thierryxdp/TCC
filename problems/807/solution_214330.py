def conta_frases(texto):
    '''Função que retorna o número de frases de um texto. Considera que as frases terminam
    com '.','!','?' e '...' e as pontuações não devem estar repetidas no texto.
    Entrada: srt. Saída: int.'''
    p = str.count(texto,' . ')
    e = str.count(texto,' ! ')
    i = str.count(texto,' ? ')
    r = str.count(texto,' ... ')
    return len(p) + len(e) + len(i) + len(r)