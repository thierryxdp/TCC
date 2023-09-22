# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    """Função que retorna uma comparação entre os valores inseridos em (a) se é igual a (b)."""
    if str(a) == str(b):
		return str(a)+str(b)
	elif str(a)!=str(b):
		return False