def conta_numero(numero,matriz):
    ''' função que dado um número inteiro e uma matriz de inteiros
    de tamanho qualquer, conta e retorna quantas vezes aquele numero
    aparece na matriz. int, list -> int'''
    r = 0
    for a in range (len(matriz)):
        for b in range (len(matriz[a])):
            if matriz[a[b] == numero:
                      r = r + 1
    return r