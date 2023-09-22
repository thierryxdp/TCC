def faltante(L):
    """funcao que calcula e retorna a peca do quebra cabeca que falta dada
       uma lista L com N-1 elementos inteiros de pecas
       
       list->int
    """
    indice=0
    while indice<len(lista):
        if lista[0]==2:
            return 1
        elif lista[indice]-1!=lista[indice-1] and lista[indice]>1:
                return lista[indice]-1
        indice=indice+1
    return lista[-1]+1