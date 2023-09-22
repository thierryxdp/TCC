def colchao(medidas,H,L):
    """Função em que dada a altura(h) e a largura(L) de um colchão, em centímetros e inteiro, retorne true se o colchão passar pela porta, ou false caso o contrário;int,int=>bool"""
	a=medidas[0]
    b=medidas[1]
    c=medidas[2]
    if a<=H and b<=L:
        return True
    elif a<=H and c<=L:
        return True
    elif b<=H and c<=L:
        return True
    elif c<=H and b<=L:
        return True
    elif a<=L and c<=H:
        return True
    elif a<=L and b<=H:
        return True
    else:
        return False