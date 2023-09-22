def colchao(medidas,H,L):
    """função que recebe medidas de um colchão e a altura
    e largura da porta de uma determinada casa e essa função
    informa se o colchão passa ou não pela porta
    list,int,int -> bool"""
    if medidas[1] > H and medidas[1] > L:
        passa = False 
        return passa
    else:
        passa = True
        return passa