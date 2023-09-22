# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
	medMin = medidas[0]
    medMid = medidas[1]
    lmin = min(H,L)
    lmax = max(H,L)
    if medMid<=lmax and medMin<=lmin:
        return True
    else:
        return False