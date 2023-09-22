def colchao(medidas, H, L):
    """Função que recebe três dimensões de um colchão 
    e verifica se ele passa pela porta de altura H e largura L.
    list -> bool"""
	if list(medidas)[1] <= H:
    	return True
	else:
        return False