def faltante(lista):
    """Retorna o número (inteiro) que falta numa dada lista.
    Entrada: lista
    Saída: int
    """
    Y = lista[:]
    list.sort(Y)
    contagem = 0
    peca = -1
    while contagem < len(Y):
        if Y[contagem] == contagem+1:
            contagem += 1
        else:
            peca = contagem + 1
            contagem = len(Y)
    if peca == -1:
        peca = len(Y) + 1
        
    return peca