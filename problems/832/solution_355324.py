def eh_quadrada(matriz):
    '''Retorna True se a matriz dada é quadrada e False caso contrário;
    list -> bool'''
    if len(matriz)==0:
        return True
    else:
        return len(matriz)==len(matriz[0])