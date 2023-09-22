def conta_numero(x,matriz):
    """Função que dado um número inteiro x e uma matriz qualquer, retorna quantas
    vezes o número apareceu na matriz.
    int, list(list) -> int
    """
    soma = 0
    for linha in matriz:
        for aij in linha:
            if aij == x:
                soma += 1
    return soma