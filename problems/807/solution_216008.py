def conta_frases(texto):
    '''recebe uma string e retorna o número de frases que ela possui retorna:
    str -> int'''
    
    texto = texto.split('.')
    texto = texto.split('?')
    texto = texto.split('!')
    texto = texto.split('...')
    
    return len(texto)