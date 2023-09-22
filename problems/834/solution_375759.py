def media_matriz(matriz):
    """Função que calcula a qauntidade de vezes que se repete um nmuero dentro de uma matriz dados de entrada e retorna a quantidade de vezes
    int , list -> int"""
    total=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            total = total + matriz[i][j]
    media = total/ (len(matriz)*len(matriz[0]))        
    return round(media,2)