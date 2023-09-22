def colchao(medidas,H,L):
    """funçao que retorna se um colchao de determinadas medidas passa por uma porta com determinadas medidas;list->True False"""
    if medidas[0]<L and medidas[2]<H:
        return True
    elif medidas[0]<L and medidas[1]<H:
        return True
    elif medidas[1]<L and medidas[0]<H:
        return True
    else:
        return False