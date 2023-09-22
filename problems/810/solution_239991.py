def inverte(frase):
    '''Entre com uma frase para ser retornado a mesma frase na ordem inversa
    String -> String'''
    
    X=frase.lower()
    esp=X.split(' ')
    esc=X.split('!')
    w=list.reverse(esc)
    a3 = ' '.join(esc)

    return a3