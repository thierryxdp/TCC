def conta_numero(numero,matriz):
    '''Dado um número inteiro e uma matriz de números inteiros, retorna quantas vezes o número aparece na matriz.
  int, matriz -> int'''
    
    soma = 0
    for x in range(len(matriz)):
        n = matriz[x].count(numero)
        soma = soma + n
    return soma