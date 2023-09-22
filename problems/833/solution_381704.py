def conta_numero(numero, matriz):
    '''Dado uma matriz de inteiros e um número inteiro, retorna quantas
    vezes esse número aparece na matriz
    
    list, int -> int'''

    numLinhas = len(matriz)

    contaNumero = 0
    
    for i in range(numLinhas):
        numeroNaLinha = list.count(matriz[i], numero)
        contaNumero = contaNumero + numeroNaLinha

    return contaNumero