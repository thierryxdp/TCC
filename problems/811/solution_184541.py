def colchao(medidas,H,L):
    """Este programa recebe uma lista com as dimensões de um colchão e recebe a altura e a largura de uma porta e verifica se o colchão passaria por esta porta
    list,int,int -> bool"""
    A = medidas[0]
	B = medidas[1]
	C = medidas[2]
	if C < L:
    	return True
    elif C < H and C < L:
        return True
    elif C > H and C < L:
        return True
    elif C < H and C > L:
        return True
    elif B < L:
    	return True
    elif B < H and C < L:
        return True
    elif B > H and C < L:
        return True
    elif B < H and C > L:
        return True
    elif B <= H:
    return True
    else:
        return False