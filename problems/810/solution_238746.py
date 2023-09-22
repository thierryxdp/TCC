def inverte(texto):
    '''retorna o texto de entrada com as palavras invertidas;
    	string->string'''
    textin=str.lower(texto)
    textoesp=str.replace(textin,',',' ')
    textoesp1=str.replace(textoesp,'.',' ')
    textoesp2=str.replace(textoesp1,'!',' ')
    textoesp3=str.replace(textoesp2,'?',' ')
    textosep=str.split(textoesp3)
    textoinv=str.join(' ',textosep[-1:])
    return textoinv