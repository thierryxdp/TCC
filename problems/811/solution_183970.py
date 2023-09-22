# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    '''
    '''
    hipot = (H ** 2 + L ** 2) ** (1 / 2)
    hipot2 = (float(medidas[0]) ** 2 + float(medidas[1]) ** 2) ** (1 / 2)
    hipot3 = (float(medidas[1]) ** 2 + float(medidas[2]) ** 2) ** (1 / 2)
    hipot4 = (float(medidas[0]) ** 2 + float(medidas[2]) ** 2) ** (1 / 2)
    if hipot <= hipot2 or hipot <= hipot3 or hipot <= hipot4:
        return True
    else:
        hipot <= hipot2 or hipot <= hipot3 or hipot <= hipot4:
        	return False