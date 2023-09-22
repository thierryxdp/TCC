def media_matriz(matriz):
    """ Dada uma matriz de inteiros não vazia, retorna a média de 
    todos os números da matriz com exatamente duas casas decimais de precisão
    list(list) -> float """
    nElementos = 0
    totalElementos = 0
    for linha in matriz:
        for elemento in linha:
            totalElementos+=elemento
            nElementos+=1
    return round(totalElementos/nElementos,2)