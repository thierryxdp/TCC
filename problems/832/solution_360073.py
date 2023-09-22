def eh_quadrada(m):
    """Função que dada uma matriz(m), retorna se ela é quadrada ou não.
    list --> bool"""
    if len(m) == len(m[0]):
        return True
    else:
        return False