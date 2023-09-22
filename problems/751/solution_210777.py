# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
	"""
    uma funçao que dada uma frase, retorna o numero de palavras
    da frase, considerando os espaços no inicio e final
    :param frase: str
    :return: int
    """
    return len(str.split(frase))