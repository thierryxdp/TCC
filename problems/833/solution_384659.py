def conta_numero(numero, matriz):
    """Dado um numero inteiro e uma matriz, conta e retorna
    quantas vezes aquele numero aparece na matriz;
    int, list -> int"""
    resposta = 0
    for linha in matriz:
        resposta += list.count(linha, numero)
    return resposta