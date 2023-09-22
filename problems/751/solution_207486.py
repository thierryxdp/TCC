# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """
    Função que recebe uma frase e retorna quantas palavras ela possui.
    str -> int
	"""
    frase = frase.split()
    return len(frase)