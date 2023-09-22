def colchao(medidas,H,L):
    """
    	Função que determina se o colchão passa pela porta ou não.
    	A entrada deve ser dada toda em centímetros.
    	list,int,int -> bool
    """
    if H>=medidas[1]:
        return True
    elif L>=medidas[2]:
        return True
    else:
        return False