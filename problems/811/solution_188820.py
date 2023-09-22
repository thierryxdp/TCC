def colchao(A,B,C,H,L):
    """Função que retorna se é possível o colchão entrar no quarto"""
    if B or C <= H or L:
        return True
    elif B or c > H or L:
        return False