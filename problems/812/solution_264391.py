def retira_pontuacao(frase):
	'''Retorna a frase dada substituindo os caracteres de
    pontuação por espaço'''
    oracao=frase
    if str.find(str(frase),'.')!=0 and str.find(str(frase),',')!=0:
       str.replace(str(oracao),'.',' ') and str.replace(str(oracao),',',' ')
    if and str.find(str(frase),'-')!=0:
       str.replace(str(oracao),'-',' ')
    return oracao