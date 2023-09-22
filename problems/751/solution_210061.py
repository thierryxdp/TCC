# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    '''
    	Recebe uma frase e conta a quantidade de palavras contidas nela
        Parâmeto 1: string
        Resultado: int
	'''
    lista = str.split(frase)
    palavras = len(lista)
    return palavras