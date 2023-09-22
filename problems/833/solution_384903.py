def conta_numero(numero, matriz):
    """Conta a quantidade de vezes que um dado número aparece na matriz dada como entrada.
    Sendo número inteiro e uma matriz de número também inteiros
    numero -> int
    matriz - list
    contador -> int
    """
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if numero == matriz[i][j]:
                contador = contador + 1
    return contador