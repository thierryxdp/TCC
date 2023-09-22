def media_matriz(matriz):
    '''funçã que dada uma matriz de inteiros não vazia, 
    calcula e retorna a média de numeros da matriz
    parametros:
    list -> float'''
    soma = 0
    tamanho = 0
    for linha in matriz:
        soma += sum(linha)
        tamanho += len(linha)
        media = soma / tamanho
        media2= round(media,2)
    return media