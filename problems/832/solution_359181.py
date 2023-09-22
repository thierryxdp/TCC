def eh_quadrada(matriz):
    """funcao que define se uma 
    matriz e quadrada.Entrada matriz
    saida string"""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i!=j:
                return False            
            if i==j:
                return True