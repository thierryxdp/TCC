def conta_frases(texto):
    '''função que retorna numero de frases dentro do texto'''
    return str.count('.') + str.count('!') + str.count ('?') + str.count ('...')