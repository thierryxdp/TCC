# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def conchao(medidas, H, L):
    """ Funcao que define se um colchao dado as suas medidas passa pela porta de altura H e largura l paralelo ao chao;
    	list, float, float -> bool
    """
	if medidas[0] <= H and medidas[1] <= L or medidas[1] <= H and medidas[2] <= L or medidas[2] <= H and medidas[0] <= L or medidas[1] <= H and medidas[0] <= L or medidas[2] <= H and medidas[1] <= L or medidas[0] <= H and medidas[2] <= L:
    	return True
    
    return False