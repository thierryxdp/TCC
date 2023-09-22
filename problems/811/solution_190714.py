# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
	medMin = medidas[0]
    medMid = medidas[1]
    if medMid<=H and medMin<=L:
        return True
    else:
        return False