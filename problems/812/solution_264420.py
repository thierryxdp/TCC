def retira_pontuacao(frase):
	'''Retorna a frase dada substituindo os caracteres de
    pontuação por espaço'''
    oracao=frase
    if str.find(str(frase),'.')!=0:
       str.replace(str(oracao),'.',' ')
     elif str.find(str(frase),',')!=0:
       str.replace(str(oracao),',',' ')
     elif str.find(str(frase),'-')!=0:
       str.replace(str(oracao),'-',' ')
     elif str.find(str(frase),'?')!=0:
       str.replace(str(oracao),'?',' ')
     elif str.find(str(frase),'!')!=0:
       str.replace(str(oracao),'!',' ')
      else:
       return oracao