def eh_quadrada(matriz):
    '''Esta e a funcao que calcula
se uma matriz e quadrada ou nao e retorna
um valor booleano indicando'''
    for linha in matriz:
        if len(linha) != len(matriz):
            return False
        elif matriz==[]:
            return True
        else:
            return True