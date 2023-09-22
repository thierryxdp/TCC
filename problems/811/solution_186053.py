def colchao(lista,H,L):
    """essa função recebe as medidas de um colchão e de uma porta como entrada e retorna o valor booleano para saber se  o colchão passa ou não pela porta;
    list,int,int--->bool"""
    X= ((lista[0]*lista[1]*2)+(lista[0]*lista[2]*2)+(lista[1]*lista[2]*2))
    if H*L>=X:
    	return True
    else:
       	return False