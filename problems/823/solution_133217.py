def faltante(lista):
    '''Funcao que retorna o qual a peca faltante do quebra cabeca.
    list->int'''
    n=0
    y=0
    z=len(lista)
    k=list(range(1,z+1))
    while y<z:
        if k[y] not in lista:
            n=n+k[y]
        y=y+1
        return n