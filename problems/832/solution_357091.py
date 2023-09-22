def eh_quadrada(matriz):
    ''' Retorna True se a matriz é considerada Quadrada, ou False se a Matriz não é considerada Quadrada'''
    linha = len(matriz)
    for linha in matriz:
        if len(linha) != linha:
            return False
    return True