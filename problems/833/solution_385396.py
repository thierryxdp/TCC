def conta_numero(numero,matriz):
    """Função que, dado um numero inteiro e uma matriz de inteiros de tamanho qualquer, retorna quantas vezes aquele número aparece na matriz
    entrada: int, list
    saída: int"""
    qntd_vezes=list.count(matriz,numero)
    return qntd_vezes