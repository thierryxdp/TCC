def inverte(frase):
    '''Entre com uma frase para ser retornado a mesma frase na ordem inversa
    String -> String'''
    x=frase.lower()
    
    y = x.split('.')
    y2 = x.split('!')
    y3 = x.split('?')
    y4 = x.split(',')
    y5 = x.split('...')
    
    
    z = ''.join(y)

    return y[-1:0]