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
    maiuscula = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minuscula = 'abcdefghijklmnopqrstuvwxyz'
    for x in range(len(maiuscula)):
    	frase = frase.replace(maiuscula[x],minuscula)
    return retira_pontuacao(frase)