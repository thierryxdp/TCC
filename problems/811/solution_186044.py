def colchao(list,H,L):
    """essa função recebe as medidas de um colchão e de uma porta como entrada e retorna o valor booleano para saber se o colchão passa ou não pela porta;
    list,int,int--->bool"""
    X= int(list[1])
    Y= int(list[0]*list[2])
    if H>=X:
    	return True
    elif Y>H:
        return True
    else:
       	return False