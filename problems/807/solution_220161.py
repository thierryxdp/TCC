def conta_frases(texto):
    '''conta o numeros de frases que aparece no texto apresentado'''
    if '...' in texto:
        texto.replace('...','.'
        return len(texto.split('.'))+ len(texto.split('!'))-1 +len(texto.split('?'))
    else:
        return len(texto.split('.'))+ len(texto.split('!'))-1 +len(texto.split('?'))-1-1