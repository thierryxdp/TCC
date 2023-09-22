def colchao([A,B,C],H,L):
    """Função que retorna se é possível o colchão entrar no quarto"""
    if B or C <= H or L:
        return True
    else:
        return False