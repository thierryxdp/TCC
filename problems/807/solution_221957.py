def conta_frases(texto):
    '''Recebe uma string e retorna quantas frases ela têm; string->string'''
    texto2=str.strip(texto,'...')
    a=str.count(texto,'...')
    b=str.count(texto,'!')
    c=str.count (texto2,'.')
    d=str.count(texto,'?')
    return a+b+c+d