# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
	wordfreq = []
	wordlist = frases.split()
	for w in frases:
    	wordfreq.append(frases.count(w))
return ("Pares\n" + str(list(zip(wordlist, wordfreq))))