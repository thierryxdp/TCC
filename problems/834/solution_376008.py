#Questao3
def media_matriz(matriz):
    '''
    A função retorna a media de todos
    os valores.
    list -> float
    '''
    soma=0
    vezes =0
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            soma += matriz[l][c]
            count += 1
            x = soma/count
                
    return float(x,2)