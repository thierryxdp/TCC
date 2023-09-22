def colchao(medidas,H,L):
	"""função que recebe as medidas do colchão e de tamanho da porta e retorna e o mesmo passa ou não
    lista,int,int->bool"""
  
    return (medidas[0]<=H and (medidas[1]<=L or medidas[2]<=L)) or (medidas[1]<=H and (medidas[0]<=L or medidas[2]<=L)) or (medidas[2]<=H and (medidas[0]<=L or medidas[1]<=L))