def faltante(L):
    '''
    Funcao que dada uma lista com N-1 inteiros numerados de 1 a N, desocbre qual
    número inteiro deste intervalo está faltando
    lista -> int
    '''
    
    if 1 not in L:
        return 1
        
    faltante=0
    n=0
    
    while n<(len(L)-1):
        if L[n]!=L[n+1]-1:
            faltante=faltante+(n+2)
        n=n+1
    if faltante==0:
               return L[-1]+1
            
    return faltante