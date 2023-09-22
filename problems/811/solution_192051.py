def colchao(medidas, H, L):
    """
    Função recebe as medidas de uma porta e de um colchão
    e verifica se o colchão passa ou não pela porta.
    lista, inteiro, inteiro --> boolean
    """
    A, B, C = medidas
    if L > B and H > A or L > A and H > B or L > C and H > A or L > A and H > C or L > B and H > C:
        return 0 == 0
    else:
        return 0 != 0