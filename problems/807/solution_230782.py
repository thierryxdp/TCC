def Nfrases (texto):
    '''função, dado um texto, retorna o número de frases que constam no texto informado
    str -> int'''
    exclamacao=str.count(texto,'!')
    interrogacao=str.count(texto,'?')
    ponto=(str.count(texto,'.'))-((str.count(texto,'...'))*3)
    reticencias=str.count(texto,'...')
    return exclamacao+interrogacao+ponto+reticencias