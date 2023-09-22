def colchao(medidas, H, L):
    """
    Função recebe as medidas de uma porta e de um colchão
    e verifica se o colchão passa ou não pela porta.
    lista, inteiro, inteiro --> boolean
    """
    A, B, C = medidas
    if L >= A and L >= B and L >= C or H >= A and H >= B and H >= C:
        return 0 == 0
    else:
        return 0 != 0