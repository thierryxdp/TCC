def retira_pontuacao(frase):
    '''Entre com uma frase para ser retornado a mesma frase na ordem inversa
    String -> String'''
    
    x=frase.lower()
    
    y = x.split('.')
    
    a = y.split('!')
    b = a.split(',')
    c = b.split('.')
    
    z = ''.join(c)

    return z