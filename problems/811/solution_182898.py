def colchao(medidas,H,L):
    """função que dada as medidas do colchão e a altura e largura da porta retorna se o colchão passa ou não pela porta;
    list,int,int -> bool"""
    if medidas[2]<H and medidas[1]<L:
        return "True"
    elif medidas[0]<L and medidas[1]<H:
        return "True"
    else:
        return "False"