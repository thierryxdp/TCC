def conta_frases(texto):
    '''retorna a quantidade de frases no texto;
    	string->int'''
    sep=str.replace(texto,'...','#')
    sep1=str.replace(sep,'.','#')
    sep2=str.replace(sep1,'!','#')
    sep3=str.replace(sep2,'?','#')
    return len(str.split(sep3,'#'))-1