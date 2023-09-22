def colchao(medidas,H,L):
    """essa função recebe as medidas de um colchão e de uma porta e retorna o valor booleano para saber se o colchão passa ou não pela porta;
    tuple,int,int--->bool"""
    X= int((medidas[1]*medidas[2]+medidas[0]*medidas[1]+medidas[0]*medidas[2])*2)
    if H*L>X:
    	return True
    else:
       	return False