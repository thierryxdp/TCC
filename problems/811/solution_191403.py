def colchao(medidas, H, L):
    """Função que recebe três dimensões de um colchão 
    e verifica se ele passa pela porta de altura H e largura L.
    list -> bool"""
	x = medidas[0]
    y = medidas[1]
    z = medidas[2]
    if x <= L and y <= H or y <= L and x <= H:
        return True
    else:
        return False