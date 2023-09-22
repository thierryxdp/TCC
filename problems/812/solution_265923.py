def retira_pontuacao(frase):
    '''.'''
    characters = "-,: ; !?"
	for x in range(len(characters)):
    	frase = frase.replace(characters[x]," ")
    return frase