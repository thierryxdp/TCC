def quadrada(matriz):
    '''funcao que identifica mariz quadrada
    entrada-matrissaida boleano'''
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i==j:
                return True
            if i!=j:
                return False
            if i==0:
                return True