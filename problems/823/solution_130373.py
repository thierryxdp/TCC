def faltante(L):
    """funcao que calcula e retorna a peca do quebra cabeca que falta dada
       uma lista L com N-1 elementos inteiros de pecas
       
       list->int
    """
    indice=0
    while indice<len(L):
        if L[0]==2:
            return 1
        elif L[indice]-1!=L[indice-1] and L[indice]>1:
                return L[indice]-1
        indice=indice+1
    return L[-1]+1