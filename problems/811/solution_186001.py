def colchao(tuple,H,L):
    """essa função recebe as medidas de um colchão e de uma porta e retorna o valor booleano para saber se o colchão passa ou não pela porta;
    tuple,int,int--->bool"""
    X= int(tuple[1])
    if H>=X:
    	return True
    else:
       	return False