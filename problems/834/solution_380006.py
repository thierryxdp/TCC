def media_matriz(matriz):
    """Recebe uma raiz de números inteiros e não vazia e retorna o valor da média de seus números com duas casas decimais de precisão;
    	list(list) -> float"""
    soma=0
    total=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma=soma+matriz[i][j]
            total=total+1
    media=soma/total
    return round(media,2)