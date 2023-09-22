def faltante(n):
    """Função quer retorna o número que falta em um dado intervalo n-1."""
    """list -> Int"""
    i = 0
    peca_faltando = 0
    n.sort()
    while i <= len(n)-1:
        if n[i]+1 != n[i+1]:
            peca_faltando = n[i]+1
        i = i+1
    return peca_faltando