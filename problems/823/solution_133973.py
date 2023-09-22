def faltante(L):
    ''' Função que dada uma lista (L) com tamanho N-1 inteiros numerados
    de 1 a N, retorna o número inteiro X que falta a L.
    Entrada: list
    Retorno: int '''

    list.sort(L)
    lista_completa = list(range(1,L[-1]+1))
    x = 0
    indice = 0
    while indice < len(lista_completa):
        if lista_completa[indice] not in L:
            x = x + lista_completa[indice]
        indice = indice + 1

    return x