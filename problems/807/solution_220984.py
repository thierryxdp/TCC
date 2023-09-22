def conta_frases():
    '''retorna quantas frases foram passadas pelo usuário a partir do termo "txt'''
        return texto.count('!') + texto.count('.') + texto.count('?') - 2*texto.count('...')