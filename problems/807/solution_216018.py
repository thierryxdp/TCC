def conta_frases(texto):
    '''recebe uma string e retorna o número de frases que ela possui retorna:
    str -> int'''
    
    texto = texto.replace('?', '.')
    texto = texto.replace("...", '.')
    texto = texto.replace('!', '.')
    texto = texto.rstrip('.')
    return texto.split('.')