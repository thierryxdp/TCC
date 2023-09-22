def faltante(L):
    '''funcao que dada uma lista N-1 inteiros numerados de 1 a N, retorna o numero inteiro faltando deste intervalo;
    list->int'''
    if L[0]!=1:
        return 1
    i=0
    while i<(len(L)-1):
        if L[i]+1==L[i+1]:
            i= i+ 1
        else:
            return L[i]+1
    else:
        return len(L)+1