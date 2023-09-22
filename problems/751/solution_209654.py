# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
	"""
    Faca uma funcao que dada uma frase, retorne o numero de palavras da frase. 
    Considere que a frase pode ter espacos no inicio e no final.
    string -> int
    """
    #frase = str.strip(frase)
    frase = str.split(frase)
    return len(frase)