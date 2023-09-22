def retira_pontuacao(frase):
	'''Retorna a frase sem os caracteres de pontuação e os substitui por espaço'''
    if str.count(str(frase),'...',0,-1)>0:
     return str.replace(str(frase),'.',' ')