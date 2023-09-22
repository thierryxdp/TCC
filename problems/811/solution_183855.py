# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
   """ """
	if H>= medidas[0] and L>= medidas[1]:
        return True
    elif H>= medidas[2] and L>= medidas[0]:
        return True
    else:
        return False