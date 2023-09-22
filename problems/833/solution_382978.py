def conta_numero(numero,matriz):
    """recebe um numero inteiro e uma matriz de inteiros
    de tamanho qualquer, conta e retorna quantas vezes
    esse numero aparece na matriz"""
    quantidade=0
    for linha in matriz:
        quantidade=quantidade+list.count(linha,numero)
        return quantidade