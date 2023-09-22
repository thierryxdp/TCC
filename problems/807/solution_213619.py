def contandoReticencias (a,d):
    ''' a cada d, subtrai 3 em a'''
    return a-(3*d)

def conta_frases(texto):
    '''retorna o número de frases que aparecem em um texto, sendo cada frase contendo terminação em
    (./!/?/...).
    str -> int'''
    a = str.count(texto,'.')
    b = str.count(texto,'!')
    c = str.count(texto,'?')
    d = str.count(texto,'...')
    return contandoReticencias(a,d)+b+c+d