def eh_quadrada(matriz):
    '''Função que retorna se uma matriz é quadrada 
    ou não. Uma matriz vazia é considerada quadrada.
    matriz=list->bool'''
    if len(matriz)==0:
        return True
    if len(matriz)!=len(matriz[0]):
        return False
    p=0
    w=len(matriz)
    t=range(w)
    while p in t:
        if len(matriz[p])==p:
            p=p+1
    return True