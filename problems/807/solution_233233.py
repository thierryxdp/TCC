def conta_frases(texto):
    '''Retorna o número de frases contidas no texto, cada frase é 
    separada por uma pontuação'''
    t = texto.split('!')
    texto = '.'.join(f)
   
    t = texto.split('...')
    texto = '.'.join(f)
   
    t = texto.split('?')
    texto = '.'.join(f)
   
    return len(texto.split('.'))