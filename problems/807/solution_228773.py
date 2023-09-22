def conta_frases(x:str):
    '''função que conta o numero de frases que aparecem no texto.str->int'''
    if '...' in x:
        return str.count(x,'.')+str.count(x,'?')+str.count(x,'!')+str.count(x,'...')-3*str.count(x,'...')
    else:
        return str.count(x,'.')+str.count(x,'?')+str.count(x,'!')