def conta_frases(text):
    '''
        dado um texto retorna a quantidade de frases nesse texto.
        str -> int
    '''
    text0=str.strip(text,' ')
    text1=str.replace(text0,'...','.')
    text2=str.replace(text1,'!','.')
    text3=str.replace(text2,'?','.')
    return str.count(text3,'.')