def colchao(medidas,H,L):
    '''dados as medidas do colchão(medida), a altura e largura(H,L) da porta, retorna True se 
    o colchão passar pela porta e False se o colchão não passar pela porta; list, int, int -> bool'''
	if medidas[0] <= L:
        if medidas[1] <= H:
            return True
        elif medidas[2] <= H:
            return True
        elif medidas[1] <= L:
            return True
        elif medidas[2] <= L:
            return True
        else:
            return False