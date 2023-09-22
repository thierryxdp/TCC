# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    conserto1=frase.lstrip(' ')
	conserto2=conserto1.rstrip(' ')
	palavras=conserto2.split(' ')
	return len(palavras)