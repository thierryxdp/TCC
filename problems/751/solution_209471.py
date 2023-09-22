# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase: str) -> int:
    '''
    Retorna quantidade de palavras dada uma frase
    '''
    separar = frase.split( )
	return len(separar)