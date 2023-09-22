# recebe uma string e retorna um dicionario falando quantas vezes cada palavra apareceu na frase
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(sentenca):
    palavras = sentenca.split()
    dicionario = {}
    contador = 0
    for elementos in palavras:
        dicionario[palavras[contador]] = palavras.count(palavras[contador])
        contador += 1
	return dicionario