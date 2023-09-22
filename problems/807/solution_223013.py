def conta_frases(texto):
    '''funcao que, dado um texto, retorna o numero de frases que compoem esse texto;
    string->int'''
    texto1=str.replace(texto,'!','.')
    texto2=str.replace(texto1,'?','.')
    texto3=str.replace(texto2,'...','.')
    return str.count(texto3,'.')