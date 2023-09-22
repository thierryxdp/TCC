def media_matriz(matriz):
    '''uma função que dada uma matriz, retorna a média simples da soma de 
    todos os numeros com 2 casas de precisão.
    matriz -> float '''
    quantidade = 0
    for a in matriz:
        for b in a:
            quantidade += b
    denominador = len(matriz) * len(matriz[0])
    total = round (quantidade/denominador)
    return total