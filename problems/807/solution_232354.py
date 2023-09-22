def conta_frases(texto):
    '''retorna o numero de frases dado um texto em forma de string; str -> int'''
    lista = []
    lista[:] = texto
    frases1 = list.count(lista,'?') + list.count(lista,'!')
    frases2 = list.count(lista,'.')
    frases3 = texto.count('...')
    return frases1 + frases2 - (2*frases3)