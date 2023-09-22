def eh_quadrada(matriz):
    '''funcao que retorna um valor booleano e valida uma
    matriz como quadrada ou nao'''
    for lista in matriz:
        if len(matriz) != len(lista):         
            return False
    return True