def conta_frases(frase):
    '''Função que pega a frase de entrada e retorna quantas frase tem de acordo com a pontuação 
    str,str→int'''    
	'''Função que pega a frase de entrada e retorna quantas frase tem de acordo com a pontuação 
    str,str→int'''
    pontuacao=['!','?','.','...']
    pontuacao1= frase.count(pontuacao[0])
    pontuacao2= frase.count(pontuacao[1])
    pontuacao3= frase.count(pontuacao[2])
    if '...' in '.':
        reticencias=frase.count('.')-2
		return pontuacao1+pontuacao2+reticencias