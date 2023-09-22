def faltante(lista):
    '''Funcao que retorna o qual a peca faltante do quebra cabeca.
    list->int'''
    list.sort(lista)
    y=0
    z=1
    while y<len(lista):
        if lista[y]==z:
            z=z+1
        y=y+1
    return z