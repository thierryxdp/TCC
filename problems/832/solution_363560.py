def eh_quadrada(matriz):
    '''Verifica de a matriz é quadrada
    	list(list) -> bool'''
    for linha in matriz:
        if len(linha) == len(matriz):
            return True
    return False