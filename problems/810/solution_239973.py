def inverte(frase):
    '''Entre com uma frase para ser retornado a mesma frase na ordem inversa
    String -> String'''
    
    x=frase.lower()
    
    y=x.split(x, ' ')
    w=list.reverse(y)
    z = ''.join(w)

    return z