def conta_frases(frase):
    '''Conta e retorna o número de frases no texto digitado pelo usuário.
    str -> int'''
    return str.count(str.replace(str.replace(str.replace(frase,'...','.'),'?','.'),'!','.'),'.')