def eh_quadrada(matriz):
    '''Função que retorna se uma matriz é quadrada ou
    não. Uma matriz vazia é considerada quadrada.
    mt=lista->bool'''
    p=0
    t=len(matriz)
    c=range(t)
    if len(matriz)==0:
        return True
   	if len(matriz)!=len(matriz[0]):
        return False
    while p in c:
        if len(matriz[p])==t:
            p=p+1
    return True