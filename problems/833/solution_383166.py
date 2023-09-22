def conta_numero(numero,matriz):
    """
    Dada uma matriz, retorna-se quantas vezes o numero dado aparece nela.
    Entradas:
    	numero -> int
        matriz -> list(lists)
    Retorna: int
    """
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                soma = soma + 1
    return soma