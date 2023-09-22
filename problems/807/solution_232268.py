def conta_frase(text):
    '''retorna o numero de frases dado um texto em string.
    str -> int'''
    text1 = text
    text2 = str.replace(text1,'!','.')
    text3 = str.replace(text2,'?','.')
    text4 = str.replace(text3,'...','.')
    print(text4)
    return len(str.split(text4,'.')) - 1