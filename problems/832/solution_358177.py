#---------------------EXERCICIO 1---------------------

def eh_quadrada(matriz):
    '''Retorna se a matriz inserida é quadrada
        list -> bool'''
    if len(matriz)==len(matriz[0]):
        return True
    return False