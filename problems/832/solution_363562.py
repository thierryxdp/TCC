def eh_quadrada(matriz):
    '''Verifica de a matriz é quadrada
    	list(list) -> bool'''
    if matriz == []:
        return True
    for linha in matriz:
        if len(linha) == len(matriz):
            return True
    return False