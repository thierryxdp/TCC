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
    frase=str.join(str.split(frase),' ')
    return frase