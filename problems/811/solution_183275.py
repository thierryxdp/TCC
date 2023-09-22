def colchao (medidas, H,L):
    '''Função diz se o colchão passa pela porta ou não. 
    Necessário dar como entrada as dimensões do colchão (medidas), altura (H) e largura (L) da porta.
    tuple (list, int, int) -> boolian'''
    porta= (H, L)
	colchao1 = (medidas)
	if colchao1[1] <= porta [0] or colchao1 [2] <= porta [1]:
		return True
	else:
		return False