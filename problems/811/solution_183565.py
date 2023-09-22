# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    a=medidas[0]
    l=medidas[1]
    c=medidas[2]
 	if a<=H and (c or l)<=L:
    	return True
	if c<=H and (a or l)<=L:
        return True
    else:
        return False