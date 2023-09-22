def media_matriz(matriz):
    """Funcao que dada uma matriz de inteiros nao vazia, retorna a media 
    de todos os numeros da matriz.
    Entrada: list, int 
    Saida: float
    """
    
    quantidade = len(matriz)*len(matriz[0])
    soma = 0 
    for i in matriz:
        for j in i:
            soma += j
    return round(soma/quantidade,2)