# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Calcula e retorna a quantidade de palavras em uma frase
    	Str -> int"""
	frase.strip()
    numerodepalavras = 1
    for i in range(len(frase)):
        if frase[i] == ' ' :
        	numerodepalavras += 1
        else:
            numerodepalavras += 0
	return numerodepalavras