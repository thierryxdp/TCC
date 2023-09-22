def inverte(frase):
    '''Entre com uma frase para ser retornado a mesma frase na ordem inversa
    String -> String'''
    
    x=frase.lower()
    y=x.split(' ')
    w=list.reverse(y)
    z = ' '.join(y)

    return z