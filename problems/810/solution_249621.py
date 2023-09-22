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
    	
    str.lower(frase)
    lista = str.split(frase)
    list.reverse(lista)
    return str.join(' ', lista)