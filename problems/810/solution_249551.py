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
    return str(frase[-1])+' '+str(frase[-2])+' '+str(frase[-3])+' '+str(frase[-4]=0)+' '+str(frase[-5]=0)+' '+str(frase[-6]=0)