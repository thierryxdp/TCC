def conta_numero(numero, matriz):
    "Função que recebe um número inteiro e uma matriz de inteiros de tamanho qualquer, e conta e retorna quantas vezes aquele número aparece na matriz."
    "int, list -> int"
    soma = 0
    n = 0
    a = len(matriz)
    b = range(len(matriz))
    for n in b:
        c = matriz[n].count(numero)
        soma = soma + c
    return soma