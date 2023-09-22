def colchao(medidas,H,L):
    '''Função que retorna, a partir das medidas do colchão e da altura e largura da porta, se o colchão consegue passar
    	list(int,int,int), int, int -> bool'''
    x=medidas
    if x[1]<L and x[0]<H:
        return True
    if x[1]<L and x[2]<H:
        return True
    if x[0]<L and x[2]<H:
        return True
    if x[0]<L and x[1]<H:
        return True
    else:
        return False