def colchao(medidas,H,L):
    """Função que ao receber medidas de um colchão, retorna se o colchão passará por portas;
    list, int,  int -> bool"""
    x = medidas[0]
    y = medidas[1]
    if (y<=H and x<=L) or (y<=L and x<=H):
        return True
    else:
        return False