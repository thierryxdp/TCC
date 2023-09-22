def eh_quadrada(matriz):
    '''Verifica de a matriz é quadrada
    	list(list) -> bool'''
    for linha in matriz:
        if len(linha) == len(matriz) or len(matriz) == 0:
            return True
    return False