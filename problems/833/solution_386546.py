def conta_numero(numero,matriz):
    """ funcao que dado de entrada um numero inteiro e uma 
    matriz de inteiros de tamanho qualquer, conta e retorna quantas
    vezes aquele número aparece na matriz;
    int, list(list) -> int"""
    i = 0
    contador = 0
    while i < len(matriz):
        for n in matriz [i]:
            if n == numero:
                contador = contador + 1
        i = i + 1
    return contador