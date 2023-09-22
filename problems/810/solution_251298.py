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
    
    return len(frase[::-1]) + retira_pontuacao(frase)