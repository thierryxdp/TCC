def faltante (lista: list) -> int:
    """Recebe uma lista com N-1 posições, contendo em cada uma, um número
    diferente entre 1 e N. Retorna qual o número entre 1 e N não está conti
    do em lista."""
    peca_faltante = 1
    while peca_faltante in lista:
        peca_faltante+=1
    return peca_faltante