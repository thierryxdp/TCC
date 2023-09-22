def conta_numero(numero,matriz):
    """
    Essa função conta a quantidade de vezes que um número aparece em uma matriz
    Parametros: numero,matriz (int, lista)
    Saida: int
    """
    qtd = 0
    for i in matriz:
        for c in i:
            if c == numero:
                qtd=qtd+1
    return qtd