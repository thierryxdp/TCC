def faltante(L):
    '''Retorna o número da peça que
       está faltando, de acordo com
       a lista L de entrada;list->int'''
    i=0
    pecas=len(L)+1
    list.sort(L)
    while i<pecas:
        if i+1 not in L:
            return i+=1
        if L[i]!=i+1:
            return i+=1
        else:
            return i+=1