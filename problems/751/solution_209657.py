# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
	"""
    funcao que dada uma frase, retorna o numero de palavras da frase. 
    Considerando que a frase pode ter espacos no inicio e no final.
    string -> int
    """
    frase = str.split(frase)
    return len(frase)