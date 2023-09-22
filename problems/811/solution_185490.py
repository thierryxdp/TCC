# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
	"""Função que retorna se um colchão passa por uma porta dadas as dimensões desses dois objetos
	Entradas: lista, int, int
	Saída: bool"""
	if medidas[1] <= H or medidas[2] <= L:
		return True
	else:
		return False