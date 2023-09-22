def faltante(L):
    """Recebe uma lista com o número de peças de um quebra cabeça
    e retorna o número da peça que falta;
    list -> int"""
    peca_faltante = L[-1] + 1
    i = 1
    while i <= len(L):
        if L[i] != i:
            peca_faltante = i
        i += 1
    return peca_faltante