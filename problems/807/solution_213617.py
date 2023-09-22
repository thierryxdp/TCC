def conta_frases(texto):
    '''retorna o número de frases que aparecem em um texto, sendo cada frase contendo terminação em
    (./!/?/...).
    str -> int'''
    lista = str.split(texto)
    a = str.count(lista,'.')
    b = str.count(lista,'!')
    c = str.count(lista,'?')
    d = str.count(lista,'...')
    return a+b+c+d