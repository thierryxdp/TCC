def retira_pontuacao(frase):
	"""Recebe uma frase e retorna outra frase com todo tipo de pontuação substituido por espaços"""
    
    return frase.replace('-',' ').replace(',',' ').replace(':',' ').replace(';',' ').replace('.',' ')