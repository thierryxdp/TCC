def conta_numero(numero,matriz):
    '''função que dado um número inteiro e uma matriz
    de inteiros conta e retorna quantas vezes esse
    inteiro aparece nela'''

    quantidade = 0
    for linha in matriz:
        quantidade = quantidade + list.count(linha,numero)
    return quantidade