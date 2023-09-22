def eh_quadrada(matriz):
    '''Verifica se a matriz é no formato quadrado;
    list(list)->bool'''
    
    #n=m (é quadrada)
    
    for l in len(matriz):
        for c in len(matriz[0]):
            if l==c:
                return True
            else:
                return False