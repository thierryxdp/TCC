def eh_quadrada (matriz):
    '''função em que dada uma matriz identifique se ela é quadrada ou não;
    list -> bool'''
    if matriz==[]:
        return True
    if len(matriz)==len(matriz[0]):
        return True
    else:
        return False