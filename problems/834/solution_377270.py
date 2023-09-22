def media_matriz(matriz):
    """ Funcao que recebe uma matriz de inteiros.
    	Retorna a media de todos os numeros da matriz com duas casas decimais de precisao;
        list -> float
    """
    soma_todos_elementos_matriz = 0
    for coluna in matriz:
        for linha in coluna:
            soma_todos_elementos_matriz += linha
            
    return soma_todos_elementos_matriz / (len(matriz[0]) * len(matriz))