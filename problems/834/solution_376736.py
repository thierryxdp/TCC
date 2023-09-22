def media_matriz(matriz):
    """Dada uma matriz, retorna a media de todos os numeros presentes na matriz dada"""
    """entrada: lista(lista)
    saida: float"""
    
    soma = 0
    qnts_numeros = len(matriz)*len(matriz[0])
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma = soma + matriz[i][j]
    
    return round(soma/qnts_numeros,2)