def conta_frases(s):
    '''dado um texto, retorna o numero de frases que ele  possui;
    string --> int'''
    ponto_final = str.count(s,'.')
    exclamacao = str.count(s,'!')
    interrogacao = str.count(s,'?')
    reticencias = str.count(s,'...')

    if reticencias > 0:
        return round((ponto_final - (reticencias*2)) + exclamacao + interrogacao)
    else:
        return ponto_final + exclamacao + interrogacao