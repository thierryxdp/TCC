def eh_quadrada(matriz):
    """ funcao que define se uma matriz e 
    quadrada.Entrada_matriz,saida _string
    """
    c=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
                       if i==j:
                       return 'c eh quadrada'