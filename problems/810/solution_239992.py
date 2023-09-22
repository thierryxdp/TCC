def inverte(frase):
    '''Entre com uma frase para ser retornado a mesma frase na ordem inversa
    String -> String'''
    
    X=frase.lower()
    y=X.split(' ')
    w=list.reverse(y)
    a3 = ' '.join(y)

    return a3