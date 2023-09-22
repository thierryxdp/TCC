def conta_frases(frases):
    '''Retorna o número de frases contidas no texto, cada frase é 
    separada por uma pontuação'''
     f = frases.split('!')
    frases = '.'.join(f)
   
    f = frases.split('...')
    frases = '.'.join(f)
   
    f = frases.split('?')
    frases = '.'.join(f)
   
    return len(frases.split('.'))