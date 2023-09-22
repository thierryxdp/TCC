def conta_numero(numero,matriz):
    """
    Função que recebe um número e uma matriz, com isso, conta e retorna quantas vezes aquele 
    número aparece na matriz.
    int, list -> int
    """

    soma = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == numero:
                soma = soma + 1
    return soma