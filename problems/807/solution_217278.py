def conta_frases(frases):
    '''retorna o numero de frases que aparecem no texto; str->int'''
    return len(frases.split('.','!','?','...'))