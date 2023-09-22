def media_matriz(matriz):
    """funcao que retorna a media de todos os numeros inteiros de uma matriz;
    list(list) -> float"""

    c=0
    soma=[]

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            c+=1
            soma.append(matriz[i][j])

    return round(sum(soma)/c,2)