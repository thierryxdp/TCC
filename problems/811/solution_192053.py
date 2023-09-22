def colchao(medidas, H, L):
    """
    Função recebe as medidas de uma porta e de um colchão
    e verifica se o colchão passa ou não pela porta.
    lista, inteiro, inteiro --> boolean
    """
    A, B, C = medidas
    if H > A and L > B or H > A  and L > C or H > B and L > A or H > B and L > C or H > C and L > A or H > C and L > B:
        return 0 == 0
    else:
        return 0 != 0