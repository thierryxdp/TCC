# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def conchao(medidas, H, L):
    """ Funcao que define se um colchao dado as suas medidas passa pela porta de altura H e largura l paralelo ao chao;
    	list, float, float -> bool
    """
	if medida[0] <= H && medida[1] <= L or medida[1] <= H && medida[2] <= L or medida[2] <= H && medida[0] <= L or medida[1] <= H && medida[0] <= L or medida[2] <= H && medida[1] <= L or medida[0] <= H && medida[2] <= L:
        return True
    
    return False