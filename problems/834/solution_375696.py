def media(matriz):
    """Função que calcula a média de todos os numeros da matriz.
        matriz -> float"""
    lista=[]
    divisao=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            divisao=divisao+j
    x=divisao/2
    
    return round(x,2)