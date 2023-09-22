# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
	"""Recebe as medidas de um colchão e as medidas da porta e 
    retorna se o colchão passa ou não pela porta.
    list, int, int -> bool"""
    
    if medidas[1] > L and medidas[1] > H:
    	return False
    elif medidas[1] <= H:
        return True
    if medidas[1] <= L:
    	return True