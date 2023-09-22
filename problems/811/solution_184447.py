def colchao(medidas,H,L):
    """Diz se o colchão consegue ou não passar pela porta
    	lista,int,int -> bool
    	Parameters:
        medidas: Altura, largura e comprimento do colchão (em cm)
        H: Altura da porta (em cm)
        L: Largura da porta (em cm)
        
        Returns:
        True caso o colchão passe pela porta
        False caso o colchão não passe pela porta       
	"""
    
    if medidas[1]<=H and medidas[0]<=L:
        return True
    else:
        return False