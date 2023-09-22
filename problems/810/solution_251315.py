def retira_pontuacao(frase):
    '''Retorna a frase cujos caracteres de pontuação foram substituídos por espaço;
    str => str'''
    pontuacao = "-,: ; !?."
	for x in range(len(pontuacao)):
    	frase = frase.replace(pontuacao[x]," ")
    return frase

def inverte(frase):
    ''' ;
    str -> str'''
    frase = frase.lower()
	# reversing words in a given string
	s = frase.split()[::-1]
	l = []
	for i in s:
    	l.append(i)
	return(" ".join(l))