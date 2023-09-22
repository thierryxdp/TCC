def eh_quadrada(matriz):
    """Função que identifica se uma matriz é quadrada. 
    matriz(lista de listas)-> string"""
    if len(matriz) == len(matriz[0]):
        return 'É quadrada'