def faltante(N):
    '''funcao que dada uma lista N-1 inteiros numerados de 1 a N, retorna o numero inteiro faltando deste intervalo;
    list->int'''
    if N[0]!=1:
        return 1
    peca=1
    i=1
    while i<(len(N)-1):
        if N[i]+1==N[i+1]:
            peca=peca+1
        i=i+1
    
    return peca