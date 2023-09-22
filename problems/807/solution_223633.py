def conta_frases(frases):
    '''Tem como entrada uma sequência de frases que são
    delimitadas (final) por '.','?','!' ou '...'. A partir
    disso, a função retorna o número de frases contida
    no texto.
    str -> int'''
    
    ret = str.count(frases, '...') - 3*str.count(frases, '..') + str.count(frases, '.') + str.count(frases, '?') + str.count(frases, '!')
    
    return ret