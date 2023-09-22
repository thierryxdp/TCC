def conta_frases(texto):
    '''Recebe um texto e conta a quantidade de frases nele, considerando frases sentenças terminadas
    em ponto final, exclamação, interrogação e reticências'''
    a = str.split(texto,'...')
    a1 = str.join('',a)
    b = str.split(a1,'.')
    c = str.split(texto,'!')
    d = str.split(texto,'?')
    numfrases = len(a) + len(b) + len(c) + len(d) - 4
    return numfrases