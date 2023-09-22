def conta_numero(numero, matriz):
    '''função que, dado um número inteiro e uma matriz de inteiros, retorna
    quantas vezes aquele número aparece na matriz;
    int, list(list) -> int'''
    n = numero
    qtd_n = 0
    for linha in matriz:
        for elemento in linha:
            if elemento == n:
                qtd_n = qtd_n + 1
    return qtd_n