def media_matriz(matriz):
    """A função calcula a média de uma matriz(list) que foi passada como parâmetro na entrada e devolve
    o valor da média(float) na saída"""
    soma = 0
    contagem = 0
    for linha in matriz:
        for coluna in linha:
            soma += coluna
            contagem+=1
        
    return round(soma/contagem,2)