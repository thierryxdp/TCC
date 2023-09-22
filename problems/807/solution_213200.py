def conta_frases(frase):
    '''função que retorna a quantidade de frases que o texto possui'''
    '''str-->int'''
    frase=frase.replace('...','.')
    frase=frase.replace('?','.')
    frase=frase.replace('!','.')
    frase=str.count(frase,'.'):
        return frase