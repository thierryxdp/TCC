def colchao(medidas, H, L):
    """Verifica se um dado colchão por uma porta de medida H x L;
    lista,int,int->bool"""
    if medidas[1] <= H or medidas[2] <= H or medidas[1] <= L or medidas[2] <= L:
        return True
    else:
        return False