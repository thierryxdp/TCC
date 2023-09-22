def eh_quadrada(matriz):
    ''' funcao que verifica se uma matriz é ou  nao quadrada ou seja se esta ou nao vazia
    list-> bool'''
    lista = []
    for i in matriz:
        if len (matriz)== len(matriz[0]):
            return True
        if len (matriz) > len(matriz[0]):
            return False
        if len(matriz)< len(matriz[0]):
            return False
        if len(matriz) == len(lista):
            return False