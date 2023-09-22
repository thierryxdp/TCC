def faltante(L:list) -> int:
    """Função diz qual a peça faltante de um quebra cabeça
       
       Parameters:
       L: Lista das peças que Joãozinho possui
       
       Returns:
       Numeração da peça que falta
    """
    N = len(L) + 1
    ordena_N = list(range(1,N + 1))
    ordena_L = L
    list.sort(ordena_L)
    i = 0

    while i < N:
        if ordena_N[i] == ordena_L[i]:
            del ordena_N[i]
        i = i + 1
    return ordena_N