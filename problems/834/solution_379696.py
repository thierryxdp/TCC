def media_matriz(matriz):
    """
    Função que recebe uma matriz e retorna a média da soma dos números da matriz
    list -> float
    """
    
    soma = 0
    tamanho = 0
    
    
    for linha in matriz:
        soma = soma + sum(linha)
        tamanho = tamanho + len(linha)
    return round(soma/tamanho,2)