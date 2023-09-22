def conta_frases(texto):
    '''função que indica quantas frases há em um texto
       str -> int'''
    return str.count(texto,'?')+str.count(texto,'!')+(str.count(texto,'.')-3*(str.count(texto,'...')))+str.count(texto,'...')