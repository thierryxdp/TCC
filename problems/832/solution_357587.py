def eh_quadrada(matriz):
    '''Retorna um booleano dizendo se a matriz é quadrada ou não.
    list -> bool'''
    if matriz == []:
        return True
    contador = 0
    while contador < len(matriz):
        if len(matriz[contador]) != len(matriz):
            return False
        contador = contador + 1
    else:
        return True