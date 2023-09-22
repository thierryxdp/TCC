def conta_frases(x):
    '''função que retorna o número de frases de um texto
    str --> int'''
    lista1=0

    if '...' in x:
        lista1+=x.count('...')-x.count('.')
    if '.' in x:
        lista1+=x.count('.')
    if '?' in x:
        lista1+=x.count('?')
    if '!' in x:
        lista1+=x.count('!')
    return lista1