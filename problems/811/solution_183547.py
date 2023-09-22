# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    a=medidas[0]
    l=medidas[1]
    c=medidas[2]
	return ((a and l) or (a and c) or (c and l))<(H or L)