def conta_numero(n, mat):
    """Função que dado um número inteiro e uma matriz de inteiros
    de tamanho qualquer, conta e retorna quantas vezes esse número
    aparece na matriz.
    int,mat->int
    """
    c = 0
    for lin in mat:
        for col in lin:
            if n == col:
                c = c + 1
    return c