def conta_frases (frases):
    '''recebe uma string, calcula e retorna o número de frases contidas nela'''
    '''string->int'''
    uma = str.strip(frases, '!','?','.')
    return len(str.split(uma))