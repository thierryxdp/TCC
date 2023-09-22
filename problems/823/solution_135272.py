def faltante(L):
    """retorna a peça que está faltando no quebra-cabeças de Joãozinho"""
    """list -> int"""
    i = 0
    N = 1
    while L[i] == N:
        N += 1
    i += 1
    return N