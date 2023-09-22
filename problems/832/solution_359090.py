def eh_quadrada(mt):
    '''Função que retorna se uma matriz é quadrada ou
    não. Uma matriz vazia é considerada quadrada.
    mt=lista->bool'''
    if len(mt)==0:
        return True
   	if len(mt)!=len(mt[0]):
        return False
    p=0
    t=len(mt)
    c=range(t)
    while p in c:
        if len(mt[p])==t:
            p=p+1
    return True