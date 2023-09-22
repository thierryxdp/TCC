# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    
    if medidas[0] and medidas[1] and medidas[2] <= H or L:
        return True
    elif medidas[0] and medidas [1] or medidas [1] and medidas [2] or medidas[0] and medidas[2] <= H or L:
    	return True
    else:
        return False