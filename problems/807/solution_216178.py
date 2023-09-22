def conta_frases(texto):
    '''Conta a quantidade de frases presentes no texto recebido
    string-> int''''
    n1 = len(str.split(texto, '.'))
    n2 =len(str.split(texto, '!'))
    n3 =len(str.split(texto, '?'))
    n4 = len(r.split(texto, '...'))
    if texto[-1:] == '.':
        return n1+n2+n3+n4 - 1