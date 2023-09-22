def inverte(frase):
    '''Entre com uma frase para ser retornado a mesma frase na ordem inversa
    String -> String'''
    
    x=frase.lower()
    l = list(frase)
    l.reverse()
    y = x.split('.')
    z = ''.join(y)

    return l