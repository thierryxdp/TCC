def conta_frases (frase):
    '''Recebe um texto e retorna a quantidade de frases que aparecem
    nesse texto'''
    frase=frase.replace('!','.')
    frase=frase.replace('?','.')
    frase=frase.replace('...','.')
    frase=frase.split('.')
    return len(frase)-1