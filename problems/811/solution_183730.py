def colchao(medidas, H,L):
    """essa funcao dadas as medidas de um colchao e de uma porta,
	 determina se possivel ou nao a passagem do colchao por essa porta
	list, int, int -> bool"""
    
   	if medidas[0] and medidas[1] > H and L:
        return False
    else:
        return True