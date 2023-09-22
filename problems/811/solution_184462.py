def colchao(medidas,H,L):
    """Indica se o colchão passa ou não pela porta.
       list,int,int->bool

       Parameters:
       medidas: Uma lista com as dimensões do colchão
       H: A altura em centimetros da porta.
       L: A largura em centimetros da porta.

       Returns:
       True se o colchão passar e False se não passar.
       """
    
    if medidas[1]<=H:
        return True
    else:
        return False