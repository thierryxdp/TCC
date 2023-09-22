def eh_quadrada(matriz):
    '''função booleana que confirma se uma matriz é quadrada
    ou não; list -> bool'''
    dimensao = len(matriz)
    for elemento in matriz:
        if len(elemento) != dimensao:
            return False
    return True