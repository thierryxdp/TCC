def eh_quadrada(matriz):
    """ define se a matriz apresentada é quadrada ou não
    retorna o valor booleano"""
    for i in range (len(matriz)):
        for j in range (len (matriz)):
            if len(matriz) == len(matriz[i]):
                return True
            else:
                return False