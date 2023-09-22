def conta_frases(s):
    '''dado um texto, retorna o numero de frases que aparecem no texto;
    string --> int'''
    return str.count(s,'.') + str.count(s,'!') + str.count(s,'?') + str.count(s,'...')