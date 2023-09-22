def conta_numero(numero,mtriz):
    """recebe um numero inteiro e uma matriz de inteiros de qualquer
    tamanho e retorna quantas vezes aquele numero aparece na matriz
    int,list(list(int))->int"""
    quantidade=0
    for linha in matriz:
        quantidade=quantidade+list.count(linha,numero)
        return quantidade