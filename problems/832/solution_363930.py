def eh_quadrada(matriz):
    ''' funcao que verifica se uma matriz é ou  nao quadrada ou seja se esta ou nao vazia
    list-> bool'''
    for i in matriz:
        if len(matriz)<0:
            return True
        if len(matriz)>=0:
            return False