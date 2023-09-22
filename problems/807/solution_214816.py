def conta_frases(texto):
    '''funçao que dada um texto retorna o numero de frases que tem nesse texto'''
    texto = texto.replace('...','.')
    return texto.count(".")+texto.count("!")+texto.count("?")