def colchao(medidas,H,L):
    '''retorna se um colchão passaria por uma porta ou não,
    dadas as medidas de cada um
    list,int,int -> bool'''
    if medidas[1]>L:
        if medidas[2]<L:
            return True
        else:
        	return False
    else:
        return True