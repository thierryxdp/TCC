def conta_frases(frase):
    '''
    função que conta o número de frases que aparecem no texto;
    str -> int
    '''
    a = str.count(frase,'...')
    b = str.count(frase,'!')
    c = str.count(frase,'?')
    d = str.count(frase,'.') - 3*a
    return a+b+c+d