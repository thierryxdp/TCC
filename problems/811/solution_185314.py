# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    a,b,c = medidas
    alturacolchao = min(a,min(b,c))
    larguracolchao = min(max(A, B),min(max(A, C),max(B, C)))
    ac = alturacolchao
    lc = larguracolchao
    if lc <= L and ac <= H:
    	return True
    else:
    	return False