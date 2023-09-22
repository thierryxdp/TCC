def colchaoXporta(dimensoes,H,L):
	"""diz se o colchao passa pela porta.entra dimensoes do colchao
    (dimencoes),altura da porta(H) e largura(L);list[float,float,float],int,int
    ->booleano"""
    if L>=dimensoes[0] and H>=dimensoes[1]:
        return True
    else:
        return False