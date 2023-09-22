# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    A= medidas[0]
    B= medidas[1]
    C= medidas[2]
	x= int( min(A, min(B, C)))
	y=int(min(max(A, B), min(max(A, C), max(B, C))))
	if x <= L and y <= H:
		return "True"
    elif x => L and y <= H:
        return "True"
    elif x <= L and y => H:
        return "True"
    else:
		return "False"