def faltante(L):
    """Função que dada uma lista com n-1 inteiros numerados de 1 a n, descubra
    qual número inteiro deste intervalo está faltando. 
        
       Parameters:
       L: lista dada como entrada 
       
       Returns:
       Retorna o número que está faltando na lista, dado que:
       list -> int."""
    list.sort(L)
    if 1 not in L:
        return 1
    if L[-1]< len(L)+1:
        return len(L)+1
    faltante=0
    i=0
    while i < len(L)-1:
        if L[i+1]-L[c]>1:
            faltante=faltante+L[i]+1
        i=i+1
    return faltante