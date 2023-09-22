def conta_frases(text):
    '''Recebe uma sting text e retorna o seu número de
    frases definidas por '...', '!', '?' e '.' no seu fim
    str -> int'''
    text = text.replace('!','.')
    text = text.replace('?','.')
    text = text.replace('...','.')
    n = text.split('.')
    return len(n) - 1