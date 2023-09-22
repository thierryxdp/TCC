def conta_frases(texto):
    '''Função que conta o número de frases que aparecem em um texto dado.
    str-->int'''
    '''lista = texto.split('.' and '...' and '!' and '?')
    return len(lista)'''
    lista1 = texto.split('.')
    lista2 = texto.split('...')
    lista3 = texto.split('!')
    lista4 = texto.split('?')
    listafinal = lista1,lista2,lista3,lista4
    return len(listafinal)+1