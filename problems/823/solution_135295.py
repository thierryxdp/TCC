def faltante(L):
    """retorna a peça que está faltando no quebra-cabeças de Joãozinho"""
    """list -> int"""
    i = 0
    N = 1
    list.sort(L)
    
    while i < len(L):
        while L[i] == N:
            i += 1
            N += 1
    return N