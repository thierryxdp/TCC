# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
	frases2 = frases.split()
    frasesn = []
	for w in frases:
    	frasesn.append(frases.count(w))
	frasesn = frasesn + str(list(zip(frases2, frasesn))))
return pares