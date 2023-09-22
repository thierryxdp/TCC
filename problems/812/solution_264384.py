def retira_pontuacao(frase):
	'''Retorna a frase dada substituindo os caracteres de
    pontuação por espaço'''
    oracao=frase
    if str.find(str(frase),'.')!=0:
       str.replace(str(oracao),'.',' ')
    if str.find(str(frase),',')!=0:
       str.replace(str(oracao),',',' ')
    if str.find(str(frase),'-')!=0:
       return str.replace(str(oracao),'-',' ')