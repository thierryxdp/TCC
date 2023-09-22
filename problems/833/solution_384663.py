def conta_numero (numero, matriz):
    """Função que retorna a quantidade de vezes que um número aparece na matriz a partir de um número inteiro e uma matriz inteira
    int, list -> int"""
    quantidade = 0
    for i in matriz:
        quantidade = quantidade + list.count(i, numero)
    return quantidade