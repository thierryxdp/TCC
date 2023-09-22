"""funcao que determina se uma matriz e quadrada"""
def eh_quadrada(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i==j:
    return "matriz eh quadrada"