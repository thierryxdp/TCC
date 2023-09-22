def conta_frases(s):
    '''dada um texto retorna quantas frases esse texto tem'''
    s = s.replace('...','.')
    return str.count(s,'?') + str.count(s,'!') + str.count(s,'.')