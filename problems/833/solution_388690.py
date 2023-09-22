def conta_numero(numero,matriz):
    """Função que dado um número inteiro e uma matriz de inteiros de tamanho qualquer, conta e retorna quantas vezes aquele número aparece na matriz
    list -> int"""
    cont = sum(linha.count(numero) for linha in matriz
    return cont