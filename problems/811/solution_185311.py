def colchao(medidas,h,l):
    """Dadas as medidas das dimensões do colchão, sua altura e largura,
    retorna se o colchão a ser comprado vai passar ou não pela porta;
    list, float, float ->bool"""
    if h>l:
        if l>=medidas[0] and h>=medidas[1]:
            return True
    else:
        if h>medidas[0] and l>medidas[1]:
            return True
    return False