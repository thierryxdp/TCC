def eh_quadrada(matriz):
    '''Recebe uma matriz e identifica se a matriz é quadrada ou não.
    list -> bool'''
    mult = []
    
    for i in matriz:
        mult += [i*n]
        total = sum(mult)
    if total % 2 == 0:
        return True
    else:
        return False