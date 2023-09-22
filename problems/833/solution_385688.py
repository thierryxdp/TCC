def conta_numero(numero, matriz):
    """
    Essa função recebe um numero inteiro e uma matriz de inteiros e retorna 
    quantas vezes o número aparece na matriz;
    int, list -> int
    """
    vezes = []
    for i in matriz:
        for j in i:
            if numero == i:
                vezes.append(i)
    return len(vezes)