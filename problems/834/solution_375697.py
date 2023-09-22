def media(matriz):
    """Função que calcula a média de todos os numeros da matriz.
        matriz -> float"""
    
    divisao=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numero=matriz[i][j]
            divisao=divisao+numero
    
    x=divisao/(len(matriz)*len(matriz[0]))
    
    return round(x,2)