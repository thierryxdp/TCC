# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H , L):
	[A, B, C] = medidas
	if A and B > H and L:
        return False
	else:
        return True