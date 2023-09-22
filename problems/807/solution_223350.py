def conta_frases(frase):
    '''
    recebe uma stream e retorna por quantas frases é formada
    str->int
    '''
    return len(str.split(str.split(str.split(frase,'.'),'!')),'?'))