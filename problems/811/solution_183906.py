# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
	hipot = (H**2+L**2)**(1/2)
    if hipot<=int(mediadas[0]) or hipot<=int(mediadas[1]) or hipot<=int(mediadas[2]):
        return False
    else:
        return True