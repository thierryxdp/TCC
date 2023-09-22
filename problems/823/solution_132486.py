def faltante(l):
    """Funcao que retorna o numero inteiro que esta faltando na lista ordenada.
    list -> int"""
    l.sort()
    lista_completa = list(range(l[0],l[-1]+1))
    if l[0] != 1:
        return 1
    if l == lista_completa :
        return lista_completa[-1]+1
    posicao = 0
    while posicao < len(lista_completa):
        if lista_completa[posicao]!=l[posicao]: 
            return lista_completa[posicao]
        posicao = posicao + 1