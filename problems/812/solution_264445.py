def retira_pontuacao(frase):
	'''Retorna a frase dada substituindo os caracteres de
    pontuação por espaço'''
    oracao=frase
	str.replace(str(oracao),'.',' ')
    str.replace(str(oracao),',',' ')
    str.replace(str(oracao),'-',' ')
    return oracao