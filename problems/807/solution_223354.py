def conta_frases(frase):
    '''
    recebe uma stream e retorna por quantas frases é formada
    str->int
    '''
    nova=str.replace(frase,'...','.')
    return str.count(nova,'.')+str.count(frase,'!')+str.count(frase,'?')