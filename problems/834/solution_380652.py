def media_matriz(matriz):
    """  Função que retorna a média de todos os números
    da matriz
    Entrada: list
    Saída : float """
    soma = 0
    divisao = 0
    for i in matriz:
        soma += sum(i)
        divisao += len(i)
    return round(soma/divisao,2)