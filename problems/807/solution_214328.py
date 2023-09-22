def n_frases(texto):
    '''Função que retorna o número de frases de um texto. Considera que as frases terminam
    com '.','!','?' e '...' e as pontuações não devem estar repetidas no texto.
    Entrada: srt. Saída: int.'''
    p = str.split(texto,' . ')
    e = str.split(texto,' ! ')
    i = str.split(texto,' ? ')
    r = str.split(texto,' ... ')
    return len(p) + len(e) + len(i) + len(r)