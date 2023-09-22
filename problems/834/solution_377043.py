def media_matriz(matriz):
    """Esta função recebe uma matriz e retorna a media de todos os número da matriz """
    c = 0
    soma = 0
    lista = []
    while c < len(matriz): 
        for i in matriz[c]:
            soma += i
        c += 1
    return round(soma/(len(matriz) * len(matriz[0])),2)