def conta_numero(numero,matriz):
    """
    Essa funcao, dados uma matriz e um numero inteiros, a funcao ira retornar quantas
    vezes o numero dado aparece na matriz.
    int,list->int
    """
    contador = 0
    for linha in matriz:
        for num in linha:
            if num == numero:
                contador += 1
    return contador