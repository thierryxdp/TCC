def conta_numero(numero, matriz):
    """Recebe um número inteiro e uma matriz de números inteiros
    e retorna quantas vezes aquele número aparece na matriz;
    int, list -> int"""
    aparicoes = 0
    for linha in matriz:
        for aij in linha:
            if aij == numero:
                aparicoes += 1
    return aparicoes