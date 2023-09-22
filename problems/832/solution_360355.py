def eh_quadrada(matriz):
    '''Coloque uma matriz e o resultado será True se ela for quadrada ou False se ela não for'''
    if len(matriz)==0 or len(matriz)==len(matriz[0]):
        return True
    else:
        return False