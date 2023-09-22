def conta_frases(texto):
    ''' funcao que dado um texto conta a quantidade de frases presentes nele
    str->int'''
    x=str.replace(str.replace(str.replace(str.replace(texto,'...','#'),'.','#'),'!','#'),'?','#')
    return str.count(x,'#')