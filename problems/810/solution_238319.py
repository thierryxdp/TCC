def inverte(frase):
    '''Entre com uma frase para ser retornado a mesma frase na ordem inversa
    String -> String'''
    x=frase.lower()
    
    y = x.split('.') and x.split('!') and x.split('?') and x.split(',') and x.split('...')
    
    
    z = ''.join(y)

    return z