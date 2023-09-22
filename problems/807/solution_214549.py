def conta_frases(texto):
    '''função que recebe um texto e retorna a quantidade de frases há no texto de entrada.
    str -> int'''
    x = str.replace(texto,'...','$')
    return str.count(x,'$') + str.count(x,'.') + str.count(x,'!') + str.count(x,'?')