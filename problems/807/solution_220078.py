def conta_frases(texto):
    '''conta o numeros de frases que aparece no texto apresentado'''
    if '...' in texto:
        return len(texto.split('.'))+ len(texto.split('!'))-1 +len(texto.split('?'))-1-3
     else:
        return len(texto.split('.'))+ len(texto.split('!'))-1 +len(texto.split('?'))-1