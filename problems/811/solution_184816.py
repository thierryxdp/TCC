# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variávei
def colchao(medidas,H,L):
	s=medidas
    if s[2]<L:
    	return s[2]<L
	elif s[1]<L and s[2]<H:
        return s[1]<L and s[2]<H
    elif s[1]<H:
        return s[1]<H
    elif s[1]<L:
        return s[1]<L
    else:
        return False