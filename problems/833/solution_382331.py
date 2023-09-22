def conta_numero(numero,matriz):
    '''Função que dado um numero inteiro e uma matriz de inteiros de qualquer tamanho, conta e retorna quantas vezes o numero aparece na matriz.
    int, list(list) -> int'''
    x=0
    for n in matriz:
        for n1 in n:
            if n1 == numero:
                x = x+1
    return x