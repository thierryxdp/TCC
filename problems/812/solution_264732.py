def retira_pontuacao(frase):
    '''dada uma frase, retorna a frase com as pontuações sendo substituídas por espaço'''
    str.join(frase," ")
	return frase.replace("-"," ").replace(","," ").replace(":"," ").replace(";"," ").replace("."," ").replace("?"," ").replace("!"," ")