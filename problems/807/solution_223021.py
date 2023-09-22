def conta_frases(texto):
    """ str->int"""
    v=str.count(texto,'.')
    i=str.count(texto,'!')
    t=str.count(texto,'?')
    o=str.count(texto,'...')
    if '...' in texto:
        v=v-1*(3*o)
        return v+i+t+o
    else:
        return v+i+t+o