def conta_frases(texto):
    '''Recebe uma string e retorna quantas frases ela têm; string->string'''
    texto2=str.split(texto,'...','!','?','.')
    return len(texto2)