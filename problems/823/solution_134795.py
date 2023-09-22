def faltante(L):
    """Recebe uma lista com o número de peças de um quebra cabeça
    e retorna o número da peça que falta;
    list -> int"""
    L.sort()
    peca_faltante = 1
    i = 0
    while i < len(L):
        if i + 1 == L[i]:
            peca_faltante = L[i] + 1
        i += 1
    return peca_faltante