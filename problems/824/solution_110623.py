def uppCons(frase):
    '''retorna a frase dade com as consoantes em maiusculo
    str->str'''
    f=''
    i=0
    while i<len(frase):
        if frase[i] in 'aeiouAEIOUãéíúó':
        	f+= frase[i]
        else:
            
            f+=frase[i].upper()
        i+=1
    return f