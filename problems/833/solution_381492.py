def conta_numero(inteiro, matriz):
    """Dado um inteiro e uma matriz de inteiros, retorna quantas
    vezes aquele número aparece na matriz;
    int, list -> int"""
    aparicoes = 0
    for linha in matriz:
        for e in linha:
            if e == inteiro:
                aparicoes+=1
    return aparicoes