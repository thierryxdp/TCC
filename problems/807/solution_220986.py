def conta_frases(txt):
    '''retorna quantas frases foram passadas pelo usuário a partir do termo "txt'''
    return str(txt.count('!') + txt.count('.') + txt.count('?') - 2*txt.count('...'))