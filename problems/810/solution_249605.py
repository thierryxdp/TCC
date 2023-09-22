def inverte(frase):
	'''Retorna a frase dada substituindo os caracteres de
    pontuação por espaço'''
    if str.find(str(frase),'.')!=0:
    	frase=str.replace(str(frase),'.',' ')
    if str.find(str(frase),',')!=0:
    	frase=str.replace(str(frase),',',' ')
    if str.find(str(frase),'-')!=0:
    	frase=str.replace(str(frase),'-',' ')
    if str.find(str(frase),'?')!=0:
    	frase=str.replace(str(frase),'?',' ')
    if str.find(str(frase),'!')!=0:
    	frase=str.replace(str(frase),'!',' ')
    if str.find(str(frase),':')!=0:
    	frase=str.replace(str(frase),':',' ')
    if str.find(str(frase),';')!=0:
    	frase=str.replace(str(frase),';',' ')
    frase=str.lower(frase)
    frase=str.split(frase)
    frase=list.reverse(frase)
    return str.join(" ", str.split(frase, ' '))