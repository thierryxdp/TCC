def conta_frases(texto):
    '''recebe uma string e retorna o número de frases que ela possui retorna:
    str -> int'''
    
    texto = texto.split('.')
    texto1 = texto.split('?')
    texto2 = texto.split('!')
    texto3 = texto.split('...')
    
    return len(texto)