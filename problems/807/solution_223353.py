def conta_frases(frase):
    '''
    recebe uma stream e retorna por quantas frases é formada
    str->int
    '''
    str.replace(frase,'...','.')
    return str.count(frase,'.')+str.count(frase,'!')+str.count(frase,'?')