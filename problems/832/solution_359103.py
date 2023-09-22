def eh_quadrada(mt):
    '''Função que retorna se uma matriz é quadrada 
    ou não. Uma matriz vazia é considerada quadrada.
    matriz=list->bool'''
    if len(mt)==0:
        return True
    if len(mt)!=len(mt[0]):
        return False
    p=0
    w=len(mt)
    t=range(w)
    while p in t:
        if len(mt[p])==w:
            p=p+1
    return True