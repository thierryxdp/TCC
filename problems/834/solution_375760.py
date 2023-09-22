def media_matriz(matriz):
    """Função que calcula a media de uma matriz dada de entrada e retornar o seu valor arrednondado de duas acasas decimais
    list -> float"""
    total=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            total = total + matriz[i][j]
    media = total/ (len(matriz)*len(matriz[0]))        
    return round(media,2)