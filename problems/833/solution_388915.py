def conta_numero(numero,matriz):
    """Recebe um numero inteiro e uma matriz de inteiros e retorna quantas vezes
    o numero aparece na matriz
    [[1,2,3],[1,2,3],[1,2,3]]"""
    repeticao = 0
    for conjunto in matriz:
        for unidade in conjunto:
            if unidade == numero:
                repeticao = repeticao + 1
    return repeticao