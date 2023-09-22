# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
	int X = min(A, min(B, C)); //menor dimensao
	int Y = min(max(A, B), min(max(A, C), max(B, C))); //segunda menor dimensÃ£o
	if(X <= L && Y <= H)
		return True
    else:
		return False