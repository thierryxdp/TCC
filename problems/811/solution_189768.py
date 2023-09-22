def colchao(medidas,H,L):
    """A função retorna se o colchão passa pela porta levando em conta
    suas medidas. list-float-float-->bool"""
    if medidas[1] <= H:
        return True
    if medidas[1] <= L:
        return True
    if medidas[2] <= H:
        return True
    if medidas[2] <= L:
        return True
    else:
        return False