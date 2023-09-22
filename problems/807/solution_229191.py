def conta_frases(frase):
    '''Função que pega a frase de entrada e retorna quantas frase tem de acordo com a pontuação 
    str,str→int'''    
	'''Função que pega a frase de entrada e retorna quantas frase tem de acordo com a pontuação 
    str,str→int'''
    pontuacao=['!','?','.','...']
    pontuacao= frase.count(pontuacao[0])
    pontuacao= frase.count(pontuacao[1])
    pontuacao= frase.count(pontuacao[2])
    pontuacao= frase.count(pontuacao[3])
	return pontuacao+pontuacao+pontuacao+pontuacao-2