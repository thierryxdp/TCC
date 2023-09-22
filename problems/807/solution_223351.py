def conta_frases(frase):
    '''
    recebe uma stream e retorna por quantas frases é formada
    str->int
    '''
    return str.cout(frase,'.')+str.count(frase,'!')+str.count(frase,'?')