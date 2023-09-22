def hashtag(s):
    '''Função que coloca um \'#\'
    no início, no meio e mo final de uma string'''
	metade=int(len(s)/2)
	return '#'+s[:metade]+'#'+s[metade:]+'#'