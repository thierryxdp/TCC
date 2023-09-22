def conta_frases(txt):
    '''retorna quantas frases foram passadas pelo usuário a partir do termo "txt'''
    return txt.count('!') + txt.count('.') + txt.count('?') - 2*txt.count('...')