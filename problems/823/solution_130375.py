def faltante(L):
    """funcao que calcula e retorna a peca do quebra cabeca que falta dada
       uma lista L com N-1 elementos inteiros de pecas
       
       list->int
    """
    i=0
    while i<len(L):
        if L[0]==2:
            return 1
        elif L[i]-1!=L[i-1] and L[i]>1:
            return L[i]-1
        i=i+1
    return L[-1]+1