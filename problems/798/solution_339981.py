# A função recebe a frase e retorna um dicionário com a quantidade de cada palavra string
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
	palavras = frase.split()
	dicionario = {}
	countador = 0
	for elementos in palavras:
		dicionario[palavras[contador]] = palavras.count(palavras[contador])
		contador += 1
	return dicionario