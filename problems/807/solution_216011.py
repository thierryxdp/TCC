def conta_frases(texto):
    '''recebe uma string e retorna o número de frases que ela possui retorna:
    str -> int'''
    
    texto1 = texto.split('.')
    texto2 = texto.split('?')
    texto3 = texto.split('!')
    texto4 = texto.split('...')
    
    return len(texto1)