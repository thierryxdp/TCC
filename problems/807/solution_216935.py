def conta_frases(texto):
    '''Função que conta o número de frases de um texto, que deve, obrigatoriamente,
        ser inserido entre aspas.
        str -> int'''
    return str.count(texto,'?')+str.count(texto,'.')+str.count(texto,'!')-(str.count(texto,'...')*3)