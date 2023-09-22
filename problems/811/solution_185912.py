def colchao(medidas,H,L):
    """funcao que calcula se um determinado colchao de acordo com sua altura e largura ira passaar pela porta"""
return (medidas[0]<=H and medidas[1]<=L)or\
	(medidas[0]<=L and medidas[1]<=H)or\
	(medidas[0]<=H and medidas[2]<=L)or\
	(medidas[1]<=L and medidas[2]<=H)or\
	(medidas[1]<=L and medidas[2]<=H)