# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    a,b,c = medidas
    alturacolchao = max(a,min(b,c))
    larguracolchao = min(max(a, b),min(max(a, c),max(b, c)))
    ac = alturacolchao
    lc = larguracolchao
    if H < L:
        L==H and H==L
    if lc <= L and ac <= H:
    	return True
    else:
    	return False