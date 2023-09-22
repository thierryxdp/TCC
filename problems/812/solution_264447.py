def retira_pontuacao(frase):
	'''Retorna a frase dada substituindo os caracteres de
    pontuação por espaço'''
    oracao=frase
	return str.replace(str(oracao),'.',' ') or str.replace(str(oracao),',',' ') or str.replace(str(oracao),'-',' ')