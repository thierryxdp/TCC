# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
	if (medidas[1]<=H and medidas[2]<=L) or (medidas[1]<=L and medidas[2]<=H):
    	return true
    else:
        return false